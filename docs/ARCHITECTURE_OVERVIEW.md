# Architecture overview

```mermaid
flowchart TB
    U[User screenshots] --> I[Browser image input]
    I --> DET[Screen-type / geometry detection]
    DET --> F[Freight / Ore branch]
    DET --> G[Gemstone branch]
    DET --> R[Refinery Work Order branch]
    F --> FE[Material + Q + amount evidence]
    G --> GE[Card + Q + Xnn evidence]
    R --> RE[Grid + refinery metadata evidence]
    FE --> A[Evidence adjudication]
    GE --> A
    RE --> A
    A --> ROWS[Structured rows]
    ROWS --> SORT[Shared ordering]
    SORT --> MERGE[Optional Material + Q merge]
    MERGE --> EXP[CSV / JSON / Discord export]
    MERGE --> UEX[Optional UEX API lookup]
    CACHE[(Browser-local OCR/debug state)] -.-> A
```

Critical invariants: single-file `index.html`; no fabricated OCR values; no screenshot-filename hardcodes; correlated OCR passes are not automatically independent proof; Freight material evidence is strength-ranked; Gemstone quantity is `Xnn`; ordering is Ore A–Z → Gemstone A–Z → Q ascending; runtime PASS requires an actual runtime run.
