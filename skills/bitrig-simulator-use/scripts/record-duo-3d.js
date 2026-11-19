// Paste into a Codex Computer Use JavaScript session after selecting Bitrig.
// app = await cua.getApp("Bitrig")
// Create a run with: let recording = recordBitrigDuo(app)
// In separate tool calls, run: nodeRepl.write(await recording.next())
// Continue until done is true. If interrupted, call recording.return() to stop.
async function* recordBitrigDuo(app, holdMs = 1600) {
  const pause = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
  const state = () => app.getAXState({ emit: false, disableDiffing: true });
  const button = (tree, label) => {
    const prefix = /^\s*(\d+) button (?:\(selected\) )?(?:(?:Description|Help): )?/;
    for (const line of tree.split("\n")) {
      const match = prefix.exec(line);
      if (!match) continue;
      const name = line.slice(match[0].length);
      if (name === label || name.startsWith(label + ", ")) return Number(match[1]);
    }
  };
  async function click(label) {
    const index = button(await state(), label);
    if (index === undefined) throw new Error("Bitrig button unavailable: " + label);
    await app.click(index);
  }
  const savedFile = (tree) => /Recording Saved, (.+?\.mp4)(?:,|$)/.exec(tree)?.[1];

  const initial = await state();
  if (button(initial, "Stop Recording") !== undefined ||
      button(initial, "Cancel Recording") !== undefined) {
    throw new Error("Bitrig already has a recording in progress.");
  }
  for (const fold of ["Closed", "Partially Open", "Fully Open"]) {
    if (button(initial, fold) === undefined) throw new Error("Select an iPhone Duo preview first.");
  }
  const window = /^\s*(\d+) standard window .*Secondary Actions: Raise/m.exec(initial);
  if (window) await app.performSecondaryAction(Number(window[1]), "Raise");

  if (button(initial, "Start Recording") === undefined) {
    await click("Recording Mode");
  }
  await click("Closed");
  yield "Ready to record the closed Duo.";

  await click("Start Recording");
  try {
    yield "Bitrig is starting the recording.";
    const deadline = Date.now() + 20000;
    while (button(await state(), "Stop Recording") === undefined) {
      if (Date.now() >= deadline) throw new Error("Bitrig did not start recording.");
      yield "Waiting for the Bitrig countdown.";
    }
    await pause(holdMs);
    for (const fold of ["Partially Open", "Fully Open"]) {
      await click(fold);
      await pause(holdMs);
      yield "Recorded " + fold + ".";
    }
  } finally {
    const tree = await state();
    const stop = button(tree, "Stop Recording");
    const cancel = button(tree, "Cancel Recording");
    if (stop !== undefined) await app.click(stop);
    else if (cancel !== undefined) await app.click(cancel);
  }
  const previous = savedFile(initial);
  const deadline = Date.now() + 30000;
  do {
    const tree = await state();
    const filename = savedFile(tree);
    if (filename && filename !== previous) {
      return { stopped: true, filename };
    }
    if (button(tree, "Start Recording") !== undefined) {
      return { stopped: true, filename: null, message: "Check Bitrig's configured recording folder." };
    }
    yield "Waiting for Bitrig to export the MP4.";
  } while (Date.now() < deadline);
  throw new Error("Bitrig did not return to an idle recording state.");
}
