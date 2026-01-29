# agent-skills

A collection of specialized skills for Claude Code to enhance development workflows across various domains.

## Installation

```shell
npx skills add hocgin/agent-skills
```

## Available Skills

### Commit Organizer
**Location:** `skills/commit-organizer`

Expert Git workflow specialist that analyzes code changes and crafts clean, logical commit histories. It helps organize uncommitted changes into well-structured commits with clear, human-friendly messages.

**Use when:** You need to organize uncommitted changes into logical commits with clear messages.

**Key Features:**
- Analyzes uncommitted changes using `git status` and `git diff`
- Groups changes into logical commits (features, bug fixes, refactors, docs, config, tests)
- Creates clear commit messages following best practices
- Ensures each commit is self-contained and buildable
- Prevents sensitive data from being committed

**Example:**
```
Please help me organize these uncommitted changes into logical commits.
```

---

### Swift Composable Architecture
**Location:** `skills/swift-composable-architecture`

Expert in The Composable Architecture (TCA) by Point-Free. Helps developers write correct, testable, and composable Swift code following TCA patterns.

**Use when:** Building, refactoring, debugging, or testing iOS/macOS features using The Composable Architecture (TCA). Covers feature structure, effects, dependencies, navigation patterns, and testing with TestStore.

**Key Features:**
- TCA fundamentals: State, Action, Reducer, Store
- Modern TCA patterns with `@Reducer` macro
- Effects and dependency management
- Navigation patterns (tree-based and stack-based)
- Testing with TestStore
- Higher-order reducers for cross-cutting concerns

**Core Principles:**
- Unidirectional data flow: Action → Reducer → State → View
- State as value types
- Explicit effects
- Composition over inheritance
- Testability first

**Example:**
```
Help me implement a new feature using TCA with proper state management and testing.
```

---

### SwiftUI Animations
**Location:** `skills/swiftui-animations`

Expert in SwiftUI animations for creating smooth, performant, and accessible animations following Apple's best practices.

**Use when:** Building, debugging, or refining animations in SwiftUI iOS/macOS apps. Covers implicit/explicit animations, transitions, gesture-driven interactions, and modern iOS 17+ APIs like PhaseAnimator and KeyframeAnimator.

**Key Features:**
- Implicit animations with `withAnimation` and `.animation()`
- Explicit animations with `Animatable` protocol
- Transitions (built-in and custom)
- Gesture-driven animations
- Modern iOS 17+ APIs (PhaseAnimator, KeyframeAnimator)
- Spring animations and timing curves
- Accessibility considerations (reduced motion)

**Core Principles:**
- Animations are driven by state changes
- Transactions propagate down the view hierarchy
- Only animatable data animates
- Declarative animation approach

**Example:**
```
Help me create a smooth spring animation for this view transition that respects accessibility settings.
```

## Author

See [AUTHOR.md](./AUTHOR.md) for author information and references.

## Contributing

This project welcomes contributions for new skills and improvements to existing ones.

## License

MIT License - See individual skill directories for specific license information.
