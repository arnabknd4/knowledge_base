# Angular: Architect + Developer Revision Guide

**Flags:** `R` Required · `O` Optional · `E` Exam oriented · `L` Real life use
**Per module:** Topics (flagged) → How Angular solves it
**Baseline:** modern Angular (standalone, signals, new control flow). Check the Angular version you target; older NgModule-era topics are marked where they still matter for interviews.

---

## 1. Platform & Tooling

### Topics
- Angular CLI (`ng new / generate / build / serve / test`) — R, L
- Workspace structure (`angular.json`, `tsconfig`, `package.json`) — R, E
- Standalone components vs NgModules — R, E, L
- Bootstrapping (`bootstrapApplication`, `app.config.ts`, providers) — R, E
- Build system (esbuild / Vite builder vs webpack) — O, L
- Environments and build configurations — R, L
- Release cadence, LTS, `ng update` migrations — R, L
- Schematics — O
- Angular vs React vs Vue trade-offs — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Consistent project setup | Angular CLI + workspace conventions |
| Code scaffolding | `ng generate` schematics |
| Module boilerplate | Standalone components (no NgModule needed) |
| App-wide configuration | `ApplicationConfig` providers in `app.config.ts` |
| Upgrades | `ng update` automated migrations |
| Fast builds | esbuild-based application builder |
| Env-specific settings | Build configurations + file replacements |

---

## 2. TypeScript Essentials

### Topics
- Types, interfaces, type aliases, enums — R, E
- Generics and constraints — R, E
- Union, intersection, literal types, type guards — R, E
- Utility types (`Partial`, `Pick`, `Omit`, `Record`, `Readonly`) — R, L
- Decorators (class, property, method, parameter) — R, E
- Strict mode, `strictNullChecks` — R, L
- Modules, path aliases — R, L
- Async: Promises, `async/await` — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Type-safe components and services | TypeScript-first framework |
| Metadata for classes | Decorators (`@Component`, `@Injectable`, `@Input`) |
| Type-safe forms and routes | Typed reactive forms, typed router params |
| Catch template errors early | Strict templates (`strictTemplates`) |
| Compile-time safety | AOT compilation |

---

## 3. Components & Templates

### Topics
- Component anatomy (selector, template, styles, metadata) — R, E
- Data binding: interpolation, property, event, two-way — R, E, L
- New control flow: `@if`, `@for`, `@switch`, `@defer` — R, E, L
- Legacy structural directives: `*ngIf`, `*ngFor` — R, E
- Inputs/Outputs, signal inputs, `model()` — R, E, L
- Content projection (`ng-content`, `ng-template`, `ng-container`) — R, E, L
- Lifecycle hooks (`ngOnInit`, `ngOnChanges`, `ngOnDestroy`, `ngAfterViewInit`) — R, E, L
- `@ViewChild`, `@ContentChild`, `viewChild()` — R, E
- View encapsulation (Emulated, ShadowDom, None) — R, E
- Template reference variables, template-driven directives — R
- Pipes: built-in, custom, pure vs impure — R, E, L
- Attribute and structural directives (custom) — R, E, L
- Smart (container) vs dumb (presentational) components — R, E, L
- Host bindings, `hostDirectives` — O, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| UI as reusable units | Components |
| Sync view and data | Data binding (property, event, two-way) |
| Conditional / list rendering | `@if`, `@for` (with `track`) |
| Parent ↔ child communication | `input()`, `output()`, `model()` |
| Flexible layouts | Content projection |
| Cleanup and setup | Lifecycle hooks, `DestroyRef` |
| Style isolation | View encapsulation |
| Behaviour reuse | Custom directives, `hostDirectives` |
| Value formatting | Pipes (pure by default) |
| Lazy UI sections | `@defer` blocks |

---

## 4. Change Detection & Reactivity

### Topics
- Zone.js and how change detection triggers — R, E, L
- Default vs `OnPush` strategy — R, E, L
- Signals: `signal`, `computed`, `effect` — R, E, L
- `linkedSignal`, `resource` APIs — O, L
- Zoneless change detection — O, E
- `ChangeDetectorRef` (`markForCheck`, `detectChanges`, `detach`) — R, E
- `async` pipe vs manual subscribe — R, E, L
- Signals vs RxJS: when to use which — R, E, L
- `toSignal`, `toObservable` interop — R, L
- Avoiding `ExpressionChangedAfterItHasBeenChecked` — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Know when to re-render | Zone.js patching async APIs (or zoneless + signals) |
| Reduce checks | `OnPush` + immutable inputs |
| Fine-grained reactivity | Signals (`signal`, `computed`, `effect`) |
| Derived state | `computed()` |
| Bridge streams and signals | `toSignal`, `toObservable` |
| Auto unsubscribe | `async` pipe, `takeUntilDestroyed` |
| Manual control | `ChangeDetectorRef` |

---

## 5. Dependency Injection

### Topics
- Injectors and hierarchy (root, environment, element/node) — R, E, L
- `@Injectable({ providedIn: 'root' })` — R, E
- Provider types: `useClass`, `useValue`, `useFactory`, `useExisting` — R, E, L
- `InjectionToken` — R, E, L
- `inject()` function vs constructor injection — R, E
- Resolution modifiers (`@Optional`, `@Self`, `@SkipSelf`, `@Host`) — R, E
- Component-level providers (`providers` vs `viewProviders`) — R, E
- Multi providers (`multi: true`) — O, E, L
- Tree-shakable providers — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Loose coupling | Hierarchical DI container |
| Singleton services | `providedIn: 'root'` |
| Scoped instances | Component or route-level providers |
| Config / non-class values | `InjectionToken` |
| Swap implementations | `useClass` / `useFactory` providers |
| DI in functions | `inject()` (guards, interceptors, resolvers) |
| Smaller bundles | Tree-shakable providers |

---

## 6. Routing & Navigation

### Topics
- Router config, `provideRouter`, route params, query params — R, E, L
- Child routes, nested `router-outlet` — R, E, L
- Lazy loading (`loadComponent`, `loadChildren`) — R, E, L
- Functional guards: `canActivate`, `canMatch`, `canDeactivate`, `canActivateChild` — R, E, L
- Resolvers — R, E, L
- Preloading strategies — O, E, L
- Route input binding (`withComponentInputBinding`) — O, L
- Router events, navigation extras — R, L
- Title strategy, scroll restoration — O
- Route-level providers — O, E
- View transitions — O

### How Angular solves it
| Problem | Angular answer |
|---|---|
| SPA navigation | Angular Router |
| Smaller initial bundle | Lazy loading (`loadComponent`, `loadChildren`) |
| Protect routes | Functional guards (`CanActivateFn`) |
| Pre-fetch data | Resolvers |
| Faster later navigation | Preloading strategies |
| Params to components | `withComponentInputBinding` |
| Scoped services per feature | Route-level `providers` |

---

## 7. Forms

### Topics
- Template-driven vs Reactive forms — R, E, L
- `FormControl`, `FormGroup`, `FormArray`, `FormBuilder` — R, E, L
- Typed forms — R, L
- Built-in validators, custom sync validators — R, E, L
- Async validators — R, E, L
- Cross-field validation — R, E, L
- `ControlValueAccessor` (custom form controls) — R, E, L
- Dynamic forms — O, L
- Form state: dirty, touched, pristine, valid, pending — R, E
- `valueChanges`, `statusChanges` — R, L
- `updateOn` (`change`, `blur`, `submit`) — O, E
- Signal-based forms (newer, check version) — O

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Complex validated forms | Reactive Forms (`FormGroup`, `FormControl`) |
| Simple forms | Template-driven (`ngModel`) |
| Custom validation | `ValidatorFn`, `AsyncValidatorFn` |
| Reusable custom inputs | `ControlValueAccessor` |
| Dynamic fields | `FormArray`, `FormBuilder` |
| React to changes | `valueChanges` observables |
| Type safety | Typed Reactive Forms |

---

## 8. HTTP & API Integration

### Topics
- `HttpClient`, `provideHttpClient` — R, E, L
- Functional interceptors (`withInterceptors`) — R, E, L
- Auth token attach, refresh-token flow — R, E, L
- Global error handling, retry — R, L
- Request cancellation, `switchMap` — R, E, L
- Caching responses — O, L
- Progress events, file upload/download — O, L
- Typed responses, DTOs/models — R, L
- WebSockets, SSE — O, L
- `httpResource` (newer, check version) — O
- CORS awareness, proxy config for dev — R, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Call APIs | `HttpClient` (Observable-based) |
| Cross-cutting HTTP logic | Interceptors (auth, logging, errors) |
| Token refresh | Interceptor + RxJS (`catchError`, `switchMap`) |
| Dev CORS issues | `proxy.conf.json` |
| Fault tolerance | RxJS `retry`, `timeout`, `catchError` |
| Typed data | Generics (`http.get<User[]>()`) |

---

## 9. RxJS

### Topics
- Observable, Observer, Subscription — R, E, L
- Subject, BehaviorSubject, ReplaySubject, AsyncSubject — R, E, L
- Cold vs hot observables, `share`, `shareReplay` — R, E, L
- Creation: `of`, `from`, `interval`, `fromEvent` — R
- Transformation: `map`, `switchMap`, `mergeMap`, `concatMap`, `exhaustMap` — R, E, L
- Filtering: `filter`, `debounceTime`, `distinctUntilChanged`, `take`, `takeUntil` — R, E, L
- Combination: `combineLatest`, `forkJoin`, `zip`, `merge`, `withLatestFrom` — R, E, L
- Error handling: `catchError`, `retry`, `retryWhen` — R, E, L
- Unsubscription strategies, memory leaks — R, E, L
- Marble testing — O

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Async streams everywhere | RxJS integrated in Router, Forms, HttpClient |
| Search-as-you-type | `debounceTime` + `distinctUntilChanged` + `switchMap` |
| Parallel API calls | `forkJoin`, `combineLatest` |
| Shared state | `BehaviorSubject` in services |
| Avoid leaks | `async` pipe, `takeUntilDestroyed`, `DestroyRef` |
| Race conditions | `switchMap` (cancel) / `exhaustMap` (ignore) |

---

## 10. State Management

### Topics
- Local component state (signals) — R, E, L
- Service-based state (BehaviorSubject / signals in a service) — R, E, L
- NgRx: Store, Actions, Reducers, Selectors, Effects — R, E, L
- NgRx Entity, Router Store, DevTools — O, L
- NgRx SignalStore — O, L
- Alternatives: NGXS, Akita, TanStack Query for Angular — O
- When NOT to use a global store — R, E, L
- Immutable updates, selectors memoization — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Simple shared state | Injectable service + signals / BehaviorSubject |
| Predictable large-app state | NgRx (Redux pattern) |
| Side effects | NgRx Effects |
| Derived data | Selectors / `computed()` |
| Lightweight store | NgRx SignalStore |
| Debugging | Redux DevTools |

---

## 11. Security

### Topics
- XSS and Angular's built-in sanitization — R, E, L
- `DomSanitizer`, `bypassSecurityTrust*` risks — R, E, L
- CSRF / XSRF protection (`HttpClientXsrfModule`, `withXsrfConfiguration`) — R, E, L
- Auth flows: OAuth2/OIDC, PKCE, JWT — R, E, L
- Token storage: memory vs cookie vs localStorage trade-offs — R, E, L
- Route guards are UX, not security — R, E, L
- Content Security Policy, Trusted Types — O, E, L
- Libraries: angular-oauth2-oidc, MSAL Angular — R, L
- Dependency security (`npm audit`) — R, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| XSS | Automatic output escaping and sanitization |
| Unsafe HTML | `DomSanitizer` (use sparingly) |
| CSRF | Built-in XSRF token handling in `HttpClient` |
| Auth in SPA | OIDC library + interceptor + guards |
| Hide UI by role | Guards + structural directives (server still authorizes) |
| Secure headers | CSP + Trusted Types support |

---

## 12. Performance

### Topics
- `OnPush` + signals — R, E, L
- `trackBy` / `track` in `@for` — R, E, L
- Lazy loading routes and components — R, E, L
- `@defer` (deferrable views) — R, E, L
- Bundle analysis (source-map-explorer, `--stats-json`) — R, L
- Tree-shaking, AOT, build optimizer — R, E
- Image optimization (`NgOptimizedImage`) — R, L
- Pure pipes vs method calls in templates — R, E, L
- Virtual scrolling (CDK) — O, L
- Hydration, SSR for LCP — O, E, L
- Web Workers — O
- Core Web Vitals awareness — R, L
- Memory leak detection — R, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Too many re-renders | `OnPush`, signals, zoneless |
| Slow list rendering | `track`, CDK virtual scroll |
| Big initial bundle | Lazy routes, `@defer` |
| Heavy images | `NgOptimizedImage` |
| Slow first paint | SSR + hydration |
| Wasteful computations | Pure pipes, `computed()` |

---

## 13. Testing

### Topics
- Jasmine + Karma (legacy) / Jest / Vitest — R, L
- `TestBed`, `ComponentFixture` — R, E, L
- Testing components (DOM, inputs, outputs) — R, L
- Testing services with `HttpTestingController` — R, E, L
- Mocking dependencies, spies — R, L
- Testing async: `fakeAsync`, `tick`, `waitForAsync` — R, E, L
- Testing signals and RxJS — R, L
- Component harnesses (CDK) — O, L
- E2E: Cypress, Playwright — R, L
- Test pyramid, coverage — R, E

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Isolated component tests | `TestBed` + standalone imports |
| HTTP testing | `provideHttpClientTesting`, `HttpTestingController` |
| Async control | `fakeAsync` / `tick` |
| Stable UI tests | Component harnesses |
| Full flows | Playwright / Cypress |

---

## 14. SSR, Build & Deployment

### Topics
- SSR, SSG (prerender), CSR trade-offs — R, E, L
- Angular SSR (`@angular/ssr`), hydration, incremental hydration — O, E, L
- AOT vs JIT — R, E
- Production build, source maps, budgets — R, L
- Docker + Nginx for Angular — R, L
- CI/CD (lint, test, build, deploy) — R, L
- Hosting: Azure Static Web Apps, S3 + CloudFront, Firebase — O, L
- Runtime config (not baked at build) — R, L
- Service Workers / PWA (`@angular/pwa`) — O, L
- Environment variables handling — R, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| SEO and first paint | SSR / prerender + hydration |
| Smaller bundles | AOT + tree-shaking + budgets |
| Offline support | Angular Service Worker |
| Same build, many envs | Runtime config file loaded at startup (`APP_INITIALIZER` / `provideAppInitializer`) |
| Containerised delivery | Multi-stage Docker build + Nginx |

---

## 15. Architecture & Project Structure

### Topics
- Feature-based folder structure — R, E, L
- Core / Shared / Feature layering — R, E, L
- Smart vs dumb components — R, E, L
- Facade pattern over state — O, E, L
- Monorepo (Nx) and workspace libraries — R, L
- Micro-frontends: Module Federation, Native Federation — O, E, L
- Design system / component library (Angular Material, CDK) — R, L
- Barrel files, public API, dependency rules (lint boundaries) — O, L
- API client generation (OpenAPI) — O, L
- Standalone-first architecture — R, E
- Dependency rule: UI → state → data access — R, E
- Backend for Frontend (BFF) — O, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Large-team scaling | Feature slices + lazy-loaded routes |
| Reuse across apps | Workspace libraries (Nx / Angular CLI libraries) |
| Independent deployments | Module / Native Federation micro-frontends |
| Consistent UI | Angular Material + CDK + shared design system |
| Clear boundaries | Nx enforce-module-boundaries lint rules |
| Decoupling UI from state | Facades / SignalStore |

---

## 16. Cross-Cutting Concerns

### Topics
- Global error handling (`ErrorHandler`) — R, E, L
- HTTP error interceptor + user notifications — R, L
- Logging and monitoring (Sentry, App Insights) — R, L
- Internationalisation (i18n, Transloco / ngx-translate) — O, L
- Accessibility (ARIA, CDK a11y, focus management) — R, L
- Theming (Material theming, CSS variables) — O, L
- Feature flags — O, L
- Analytics hooks — O
- Form UX, loading and empty states — R, L

### How Angular solves it
| Problem | Angular answer |
|---|---|
| Uncaught errors | Custom `ErrorHandler` |
| API error UX | Functional HTTP interceptor |
| Multi-language | Built-in i18n or Transloco |
| Accessibility | CDK a11y (`FocusTrap`, `LiveAnnouncer`) |
| Theming | Angular Material theming + CSS variables |

---

## Mental Model (one line each)
- **Component tree:** App → Routes → Feature components → Presentational components
- **Data flow:** Inputs down, Outputs up, services for shared state
- **Reactivity:** Signals for local sync state, RxJS for async streams, `async` pipe / `toSignal` at the boundary
- **DI:** everything injectable, resolved through a hierarchy of injectors
- **Rendering:** `OnPush` + signals by default, Default only when forced
- **Performance:** lazy-load everything routed, defer everything below the fold
- **Security:** Angular escapes by default, the server decides authorization

## Top Interview Hotspots
1. Change detection: Default vs `OnPush`, Zone.js, signals, zoneless
2. Signals vs RxJS, and when to use which
3. RxJS flattening operators (`switchMap` vs `mergeMap` vs `concatMap` vs `exhaustMap`)
4. DI: hierarchy, `providedIn`, `InjectionToken`, `inject()`
5. Standalone components vs NgModules
6. Lazy loading, `@defer`, preloading
7. Reactive vs template-driven forms, `ControlValueAccessor`
8. Interceptors and token refresh flow
9. State management: service vs NgRx, when not to use NgRx
10. Performance: `track`, `OnPush`, bundle size, SSR + hydration

---

# Cut-Down Strategy

## Tier 1: Master in depth (~60% of effort)
1. Components, templates, new control flow, input/output
2. Change detection, `OnPush`, signals
3. RxJS core operators and flattening strategies
4. Dependency Injection (hierarchy, tokens, providers)
5. Routing: lazy loading, guards, resolvers
6. Reactive forms + custom validators + `ControlValueAccessor`
7. HttpClient + interceptors (auth, errors, refresh)
8. Standalone architecture and feature-based structure
9. State management decision-making (service/signals vs NgRx)
10. Security (XSS, token storage, OIDC flow)

## Tier 2: Working knowledge (~30%)
- NgRx concepts (Store, Effects, Selectors)
- Performance toolkit (`track`, `@defer`, bundle analysis)
- Testing (`TestBed`, `HttpTestingController`, Playwright)
- SSR + hydration basics
- Docker/Nginx deployment, runtime config
- Nx / workspace libraries basics
- Angular Material + CDK

## Tier 3: Awareness only (~10%)
- Micro-frontends (Module Federation)
- Zoneless internals, `resource` / `httpResource`
- Schematics, custom builders
- Web Workers, PWA/Service Worker
- i18n tooling, advanced theming
- Signal-based forms

## Drop for now
- AngularJS (1.x) concepts
- Deep Zone.js internals
- Custom compiler/renderer internals
- Legacy-only patterns (NgModule-heavy `forRoot` patterns beyond interview awareness, `ngClass`/`ngStyle` deep dives)

---

# Steady 6-Week Plan

*Assumes ~1 to 1.5 hrs/day. With less time, stretch to 8-9 weeks, same order. Do not skip Tier 1.*

| Week | Focus | Output |
|---|---|---|
| **1** | TypeScript gaps, standalone components, templates, control flow, inputs/outputs, lifecycle | Small app with parent/child components, `@for` with `track`, content projection, custom pipe and directive |
| **2** | Change detection, `OnPush`, signals, DI deep dive | Convert app to `OnPush` + signals; service with `InjectionToken` and `useFactory`; one-page notes on CD and DI hierarchy |
| **3** | RxJS core + HttpClient + interceptors | Typeahead search with `switchMap`; auth + error + loading interceptors; token refresh flow |
| **4** | Routing + forms | Lazy-loaded feature routes with guards and resolver; reactive form with async + cross-field validators and a custom `ControlValueAccessor` |
| **5** | State management, security, architecture | Same feature with service-signals state and a NgRx version to compare; OIDC login (PKCE); feature-based folder structure with a shared library |
| **6** | Performance, testing, SSR, deployment + interview revision | `@defer` + bundle analysis; component and `HttpTestingController` tests + one Playwright flow; Docker + Nginx build and CI pipeline; mock interviews on Top 10 |

## Daily rhythm
- **30 min** concept (one module)
- **45 min** hands-on (implement in the sample project)
- **15 min** revision (5 lines: problem → Angular answer → trade-off)

## Weekly checkpoints
- **Day 6:** Revise using Mental Model + Top Interview Hotspots
- **Day 7:** Explain 3 topics aloud as in an interview (why this, trade-offs, alternatives)

## Architect-standard test for every Tier 1 topic
You are ready when you can answer all four:
1. **What problem** does it solve?
2. **How** does Angular implement it?
3. **Trade-offs** and failure modes?
4. **When would you NOT use it?**