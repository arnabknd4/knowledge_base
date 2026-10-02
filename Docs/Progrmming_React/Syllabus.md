# React: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How React solves it
**Baseline:** modern React (function components, hooks, concurrent features, Server Components via a framework). Verify version-specific APIs (`use`, Actions, `useActionState`, `useOptimistic`, React Compiler) against the version you target.

---

## 1. Platform & Tooling

### Topics
- Library vs framework: what React is and is not — R, E
- Build tools: Vite, Next.js, Remix/React Router, CRA (legacy) — R, E, L
- JSX, transpilation, Babel/SWC — R, E, L
- Project structure and conventions — R, L
- TypeScript with React — R, E, L
- Linting and formatting (ESLint, Prettier, `eslint-plugin-react-hooks`) — R, L
- Strict Mode behaviour — R, E, L
- React DevTools and Profiler — R, L
- Release cadence and migration paths — O, L
- React vs Angular vs Vue trade-offs — R, E

### How React solves it
| Problem | React answer |
|---|---|
| UI as a function of state | Declarative components |
| Fast dev and builds | Vite / Next.js tooling |
| Catch hook mistakes | `eslint-plugin-react-hooks` |
| Surface unsafe patterns | `<StrictMode>` double-invocation in dev |
| Debug renders | React DevTools Profiler |
| Type safety | TypeScript generics for props/hooks |

---

## 2. JavaScript / TypeScript Essentials for React

### Topics
- Closures (stale closure bugs) — R, E, L
- Destructuring, spread, optional chaining — R
- Array methods (`map`, `filter`, `reduce`) — R, L
- Immutability (copy-on-write updates) — R, E, L
- Promises, `async/await` — R, E, L
- ES modules, import/export, dynamic `import()` — R, E, L
- `this` binding (legacy class components) — E
- TypeScript: props typing, generics, utility types, discriminated unions — R, E, L
- Reference vs value equality — R, E, L

### How React solves it
| Problem | React answer |
|---|---|
| Detect changes cheaply | Reference equality on state and props |
| Predictable updates | Immutable state updates |
| Code splitting | `import()` + `React.lazy` |
| Typed components | TS interfaces/generics for props, `ComponentProps`, `ReactNode` |

---

## 3. Components, JSX & Rendering

### Topics
- Function components, props, `children` — R, E, L
- Composition over inheritance — R, E, L
- Conditional rendering, lists, `key` prop — R, E, L
- Controlled vs uncontrolled components — R, E, L
- Fragments, portals — R, E, L
- Render phase vs commit phase — R, E
- Virtual DOM, reconciliation, diffing algorithm — R, E, L
- Why `key` must be stable and unique — R, E, L
- Refs and DOM access (`useRef`, `forwardRef`, ref as prop) — R, E, L
- Event handling, synthetic events, event delegation — R, E, L
- Class components and lifecycle (legacy awareness) — E, O
- Error Boundaries — R, E, L
- Component patterns: container/presentational, compound components, render props, HOCs, custom hooks — R, E, L
- Suspense for data/code loading — R, E, L

### How React solves it
| Problem | React answer |
|---|---|
| Reusable UI | Components + composition |
| Efficient DOM updates | Reconciliation (virtual DOM diff) |
| List identity | `key` prop |
| Escape hatch to DOM | Refs |
| Render outside parent DOM | Portals |
| Crash isolation | Error Boundaries |
| Loading UI | Suspense boundaries |
| Behaviour reuse | Custom hooks (replaced most HOCs/render props) |

---

## 4. Hooks & State

### Topics
- `useState`, functional updates, batching — R, E, L
- `useReducer` and reducer pattern — R, E, L
- `useEffect`: dependencies, cleanup, when NOT to use — R, E, L
- `useLayoutEffect` vs `useEffect` — R, E
- `useRef` (mutable value, DOM ref) — R, E, L
- `useMemo`, `useCallback`, `React.memo` — R, E, L
- `useContext` — R, E, L
- `useId`, `useTransition`, `useDeferredValue` — R, E, L
- `useSyncExternalStore`, `useImperativeHandle` — O, E
- `useActionState`, `useOptimistic`, `use` (newer, check version) — O, E, L
- Rules of Hooks and why — R, E, L
- Custom hooks design — R, E, L
- Stale closures, exhaustive-deps — R, E, L
- "You might not need an effect" patterns — R, E, L
- Lifting state up, state colocation — R, E, L
- Derived state vs stored state — R, E, L

### How React solves it
| Problem | React answer |
|---|---|
| Local state | `useState` |
| Complex transitions | `useReducer` |
| Side effects (sync with outside world) | `useEffect` with cleanup |
| Avoid wasted work | `useMemo`, `useCallback`, `React.memo` |
| Share without prop drilling | Context + `useContext` |
| Keep UI responsive | `useTransition`, `useDeferredValue` |
| Reuse stateful logic | Custom hooks |
| Subscribe to external stores | `useSyncExternalStore` |

---

## 5. Rendering Behaviour & Performance

### Topics
- What triggers a re-render (state, props, context, parent) — R, E, L
- Render optimisation: `React.memo`, `useMemo`, `useCallback` trade-offs — R, E, L
- Context re-render pitfalls and splitting contexts — R, E, L
- Key-based remounting — R, E, L
- Code splitting, `React.lazy`, route-level splitting — R, E, L
- List virtualisation (react-window, TanStack Virtual) — R, L
- Concurrent rendering, time slicing, transitions — R, E
- Batching (automatic in React 18+) — R, E
- Bundle analysis, tree shaking — R, L
- Image/asset optimisation, lazy loading — R, L
- Profiling with DevTools Profiler — R, E, L
- React Compiler (automatic memoisation) — O, E
- Core Web Vitals awareness (LCP, INP, CLS) — R, L

### How React solves it
| Problem | React answer |
|---|---|
| Too many re-renders | Memoisation, state colocation, context splitting |
| Big initial bundle | `React.lazy` + Suspense + route splitting |
| Long lists | Windowing / virtualisation |
| Janky input during heavy render | `useTransition` / `useDeferredValue` |
| Find slow components | Profiler flamegraph |
| Manual memo burden | React Compiler |

---

## 6. State Management

### Topics
- Local vs shared vs server state vs URL state — R, E, L
- Context API: strengths and limits — R, E, L
- Redux Toolkit (slices, thunks, RTK Query) — R, E, L
- Zustand, Jotai, Recoil (awareness) — R, L
- Server state: TanStack Query / RTK Query / SWR — R, E, L
- Form state: React Hook Form, Formik — R, L
- URL as state (search params) — R, L
- When NOT to use a global store — R, E, L
- Normalised state, selectors, memoised selectors — R, E, L
- Optimistic updates and cache invalidation — R, E, L
- State machines (XState) — O

### How React solves it
| Problem | React answer |
|---|---|
| Simple shared state | Context + `useReducer` |
| Large predictable state | Redux Toolkit |
| Lightweight global store | Zustand / Jotai |
| API data caching | TanStack Query / RTK Query (separate server state) |
| Forms | React Hook Form |
| Shareable UI state | URL search params |

---

## 7. Routing & Navigation

### Topics
- React Router (data routers, loaders, actions) — R, E, L
- Nested routes, layouts, outlets — R, E, L
- Route params, search params — R, L
- Protected routes / auth guards — R, E, L
- Code splitting per route — R, E, L
- Next.js routing (App Router, Pages Router) — R, E, L
- Navigation, redirects, history — R, L
- Error and loading route boundaries — R, E, L
- TanStack Router (awareness) — O

### How React solves it
| Problem | React answer |
|---|---|
| Client navigation | React Router / framework router |
| Fetch before render | Route loaders |
| Mutations tied to routes | Route actions |
| Layout reuse | Nested routes + `Outlet` |
| Lazy routes | `lazy()` route modules |
| Auth gating | Wrapper routes / loader redirects |

---

## 8. Data Fetching & API Integration

### Topics
- `fetch`, Axios — R, L
- Fetch in effects: pitfalls (race conditions, cleanup) — R, E, L
- TanStack Query: caching, staleness, retries, invalidation, mutations — R, E, L
- Suspense for data fetching, `use` hook — O, E, L
- Server Components / server actions (Next.js) — R, E, L
- Error, loading, empty states — R, L
- Request cancellation (`AbortController`) — R, E, L
- Pagination and infinite scroll — R, L
- Auth token handling, interceptors — R, E, L
- GraphQL clients (Apollo, urql, Relay) — O, E, L
- WebSockets / SSE — O, L
- API client generation (OpenAPI) — O, L

### How React solves it
| Problem | React answer |
|---|---|
| Cache + dedupe requests | TanStack Query |
| Race conditions in effects | Cleanup + `AbortController` or use a data library |
| Server-side data fetching | Server Components / loaders |
| Pagination | `useInfiniteQuery` / cursor APIs |
| Loading UX | Suspense + skeletons |
| Mutations with rollback | Optimistic updates via query library |

---

## 9. Forms & Validation

### Topics
- Controlled vs uncontrolled inputs — R, E, L
- React Hook Form — R, L
- Validation: Zod / Yup with resolvers — R, E, L
- Form state: errors, touched, dirty, submitting — R, L
- Dynamic and array fields — R, L
- File upload — R, L
- Accessibility of forms (labels, errors, focus) — R, L
- Form Actions, `useFormStatus`, `useActionState` (newer) — O, E

### How React solves it
| Problem | React answer |
|---|---|
| Performance of large forms | Uncontrolled inputs via React Hook Form |
| Schema validation | Zod + resolver (shared with backend types) |
| Server mutations from forms | Form Actions / server actions |
| Pending states | `useFormStatus`, `useTransition` |

---

## 10. Security

### Topics
- XSS: JSX escaping, `dangerouslySetInnerHTML` risk — R, E, L
- Sanitising HTML (DOMPurify) — R, E, L
- Token storage: memory vs httpOnly cookie vs localStorage — R, E, L
- OAuth2 / OIDC with PKCE, auth libraries — R, E, L
- CSRF and cookie settings (`SameSite`, `Secure`) — R, E, L
- Frontend authorization is UX, server enforces — R, E, L
- Content Security Policy — R, E, L
- Dependency security (`npm audit`, lockfiles, supply chain) — R, L
- Secrets in frontend bundles (none belong there) — R, E, L
- Third-party scripts risk — R, L
- Safe URL handling (`javascript:` URLs, open redirects) — R, E

### How React solves it
| Problem | React answer |
|---|---|
| XSS by default | Automatic escaping in JSX |
| Raw HTML needs | `dangerouslySetInnerHTML` + sanitiser |
| Auth in SPA | OIDC (PKCE) library + BFF / httpOnly cookies |
| Env secrets | Never in client code; use server/BFF |
| Supply chain | Lockfile + audit + minimal deps |

---

## 11. Rendering Strategies: CSR, SSR, SSG, Server Components

### Topics
- CSR vs SSR vs SSG vs ISR — R, E, L
- Hydration and hydration mismatch — R, E, L
- Streaming SSR and Suspense — R, E, L
- React Server Components (RSC): server vs client components — R, E, L
- `"use client"` / `"use server"` boundaries — R, E, L
- Next.js App Router, caching layers, revalidation — R, E, L
- SEO and Core Web Vitals impact — R, L
- Edge rendering — O, L
- Islands / partial hydration (awareness) — O
- Choosing a rendering strategy by use case — R, E, L

### How React solves it
| Problem | React answer |
|---|---|
| SEO and fast first paint | SSR / SSG via a framework |
| Less client JS | Server Components |
| Progressive loading | Streaming + Suspense |
| Interactive parts only | Client Components (`"use client"`) |
| Fresh yet fast pages | ISR / revalidation (framework) |

---

## 12. Testing

### Topics
- Jest / Vitest — R, L
- React Testing Library (query by role, user-event) — R, E, L
- Testing hooks (`renderHook`) — R, L
- Mocking network (MSW) — R, L
- Component, integration, E2E layers (test pyramid) — R, E, L
- E2E: Playwright, Cypress — R, L
- Snapshot testing pitfalls — R, E
- Accessibility testing (jest-axe, axe) — O, L
- Visual regression (Storybook, Chromatic) — O, L
- Testing async UI and Suspense — R, L

### How React solves it
| Problem | React answer |
|---|---|
| Test behaviour not implementation | React Testing Library |
| Realistic API tests | MSW (mock service worker) |
| Hook logic tests | `renderHook` |
| Cross-browser flows | Playwright / Cypress |
| Component documentation + visual tests | Storybook |

---

## 13. Architecture & Project Structure

### Topics
- Feature-based folder structure — R, E, L
- Component design: atomic design, design system — R, E, L
- Separation: UI / state / data access / domain logic — R, E, L
- Custom hooks as the logic layer — R, E, L
- Monorepo (Nx, Turborepo, pnpm workspaces) — R, L
- Micro-frontends: Module Federation, single-spa — O, E, L
- Shared component library, Storybook — R, L
- Dependency boundaries and lint rules — O, L
- Backend for Frontend (BFF) — R, E, L
- API contracts, OpenAPI/GraphQL codegen — O, L
- Error handling strategy, feature flags — R, L
- Monolithic SPA vs framework-based (Next.js) decision — R, E, L

### How React solves it
| Problem | React answer |
|---|---|
| Team scaling | Feature slices + shared libraries |
| Consistent UI | Design system + component library |
| Independent deployments | Module Federation micro-frontends |
| Logic reuse | Custom hooks, headless components |
| Contract safety | TypeScript + generated API clients |
| Shared tooling | Monorepo with workspaces |

---

## 14. Accessibility, Styling & UX

### Topics
- Semantic HTML, ARIA basics — R, E, L
- Keyboard navigation, focus management — R, E, L
- Styling: CSS Modules, Tailwind, styled-components/Emotion, CSS-in-JS trade-offs — R, E, L
- Theming (CSS variables), dark mode — R, L
- Component libraries: MUI, Radix, shadcn/ui, Chakra — R, L
- Responsive design, container queries — R, L
- Internationalisation (react-i18next, FormatJS) — O, L
- Animations (Framer Motion, CSS) — O, L
- Loading, empty and error states — R, L

### How React solves it
| Problem | React answer |
|---|---|
| Accessible components | Headless libraries (Radix, React Aria) |
| Scoped styles | CSS Modules / CSS-in-JS / Tailwind |
| Theming | CSS variables + context |
| i18n | `react-i18next` / FormatJS |
| Focus handling | Refs + focus management hooks |

---

## 15. DevOps & Deployment

### Topics
- Build output, environment variables at build vs runtime — R, E, L
- Docker + Nginx for SPA, Node image for Next.js — R, L
- CI/CD (lint, test, build, deploy previews) — R, L
- Hosting: Vercel, Netlify, Azure Static Web Apps, S3 + CloudFront — R, L
- CDN, caching headers, content hashing — R, E, L
- Source maps, error monitoring (Sentry) — R, L
- Feature flags, A/B testing — O, L
- Performance budgets, Lighthouse CI — O, L
- Runtime config for multi-environment builds — R, L

### How React solves it
| Problem | React answer |
|---|---|
| Static SPA hosting | Build to static assets + CDN |
| SSR hosting | Node server / serverless / edge via framework |
| Cache busting | Hashed filenames |
| Per-env config | Runtime config (not baked at build) |
| Production errors | Sentry + source maps |

---

## Mental Model (one line each)
- **Core idea:** UI = f(state); React re-runs components, diffs the output, and commits changes
- **Data flow:** props down, events up; lift state to the lowest common parent
- **Effects:** for syncing with the outside world, not for deriving data
- **Server state ≠ client state:** use a data-fetching library for the former
- **Performance:** colocate state first, memoise only measured hotspots
- **Rendering strategy:** pick CSR/SSR/SSG/RSC by SEO, freshness, and interactivity needs
- **Security:** React escapes by default; the server decides authorization

## Top Interview Hotspots
1. Reconciliation, virtual DOM, `key`, and what triggers re-renders
2. Hooks: rules, `useEffect` dependencies and cleanup, stale closures
3. `useMemo` / `useCallback` / `React.memo`: when they help and when they hurt
4. State management choices: Context vs Redux Toolkit vs Zustand vs TanStack Query
5. Controlled vs uncontrolled components and form strategy
6. Concurrent features: transitions, Suspense, `useDeferredValue`
7. CSR vs SSR vs SSG vs Server Components, and hydration
8. Performance: code splitting, virtualisation, Profiler usage
9. Security: XSS, token storage, OIDC flow in SPAs
10. Architecture: feature structure, design system, micro-frontends

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Rendering model: reconciliation, keys, re-render triggers
2. Hooks in depth: `useState`, `useEffect`, `useRef`, `useMemo`, `useCallback`, `useReducer`, `useContext`
3. Component composition and custom hooks
4. State management decision-making (local, context, Redux Toolkit/Zustand, server state)
5. Data fetching with TanStack Query (caching, mutations, invalidation)
6. Forms (React Hook Form + Zod)
7. Routing with loaders/actions and code splitting
8. Performance (memoisation trade-offs, lazy loading, virtualisation)
9. Rendering strategies: SSR/SSG/RSC with Next.js basics
10. Security (XSS, token storage, OIDC/PKCE)

## Tier 2: Working knowledge (~30%)
- Concurrent features (`useTransition`, Suspense)
- Testing (RTL, MSW, Playwright)
- Architecture: feature slices, design system, monorepo basics
- Accessibility essentials
- Styling approaches (Tailwind / CSS Modules / CSS-in-JS)
- Deployment (static hosting, Docker/Nginx, CDN caching)
- TypeScript patterns for props and hooks

## Tier 3: Awareness only (~10%)
- React Compiler, `useSyncExternalStore`, `useImperativeHandle`
- Micro-frontends, Module Federation
- GraphQL clients, XState
- Edge rendering, islands architecture
- Animation libraries, i18n tooling

## Drop for now
- Class component lifecycles beyond interview awareness
- Legacy patterns (HOC-heavy code, `componentWillReceiveProps`, CRA specifics)
- Deep React internals (Fiber source details)

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | JS/TS gaps, JSX, components, props, composition, keys, rendering model | Small app (list + filter + detail) with typed components; one-page notes on reconciliation and re-render triggers |
| **2** | Hooks deep dive: `useState`, `useReducer`, `useEffect`, `useRef`, memoisation, custom hooks | Rebuild features using custom hooks; fix a stale-closure bug and an effect race condition deliberately |
| **3** | State management + data fetching | Same app with Context + reducer, then Redux Toolkit/Zustand; add TanStack Query with caching, mutation and optimistic update |
| **4** | Routing, forms, validation | Nested routes with loaders/actions, protected routes, lazy routes; React Hook Form + Zod with dynamic fields |
| **5** | Performance, concurrent features, rendering strategies (Next.js), security | Profile and optimise renders; virtualise a long list; add `useTransition`; build an SSR/RSC page; implement OIDC (PKCE) login |
| **6** | Testing, architecture, deployment + interview revision | RTL + MSW tests and one Playwright flow; feature-based structure with shared UI library; Docker/Nginx or Vercel deploy with CI; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (implement in the sample project)
- **15 min** revision (5 lines: problem → React answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does React implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**