# Release 4.2 EU Onboarding Wave

## Overview
Release 4.2 EU Onboarding Wave — Customer rollout management, deployment tracking, readiness monitoring, and launch coordination for Release 4.2 (July 14, 2026) across 6 EU customers (BluePeak, Helio, Meridian, NordForge, UrbanNest, ClearWave).

## Problem Statement
Acme Horizon Group Release 4.2 EU onboarding rollout (June-July 2026) requires coordinated customer management:
- 50 rollout milestones tracked (6 customers, 4 phases)
- 6 EU customers: BluePeak Logistics, Helio Retail, Meridian Health, NordForge Manufacturing, UrbanNest Facilities, ClearWave Utilities
- 4 phases: Planning, UAT, Deployment, Post-Launch
- Readiness: 56.62%-95.58% (avg 78.95%)
- Training completion: 44%-98.58% (avg 73.99%)
- Customer signoff: Pending or Yes (mixed)
- Critical blockers: VAT mismatch, legacy export, training access, performance tuning
- Go-live: July 14, 2026 (target date)
- Hypercare: Post-launch support required

## Key Features
- Customer rollout tracking (6 EU customers)
- Phase management (Planning, UAT, Deployment, Post-Launch)
- Readiness % monitoring (target: >85%)
- Training completion tracking (target: >90%)
- Customer signoff workflow
- Support readiness levels (Docs → Hotline)
- Critical blocker identification and resolution
- Milestone and dependency tracking
- Launch confidence scoring
- Post-launch contingency planning

## EU Customers
- BluePeak Logistics (rollout in progress)
- Helio Retail Group (UAT phase)
- Meridian Health Supplies (UAT → Deployment)
- NordForge Manufacturing (UAT phase)
- UrbanNest Facilities (UAT → Deployment)
- ClearWave Utilities (Post-Launch ready)

## Release 4.2 Key Features
- Feature A Go-Live (UAT exit gate)
- EU VAT mapping workshop (country code fix)
- Data Migration (legacy export dependency)
- Training Complete (certification required)
- Hypercare support (72h post-launch)
- EOM invoicing dry run (Finance readiness)

## Key Metrics (June-July 2026)

### Portfolio
- Total Milestones: 50 (6 customers × phases)
- Customers: 6 (all EU)
- Phases: 4 (Planning, UAT, Deployment, Post-Launch)
- Timeline: June 3 - July 29, 2026
- Go-Live: July 14, 2026

### Readiness
- Readiness %: 56.62%-95.58% (avg 78.95%)
- Training Completion: 44%-98.58% (avg 73.99%)
- Customer Signoff: 20% Yes, 80% Pending
- Confidence Level: Mixed (on-track to at-risk)

### Critical Issues
- VAT country code mismatch (multiple customers)
- Legacy export file/delimiter issues (NordForge)
- Training tenant access blocked (Helio)
- UAT performance tuning (Meridian)
- Release 4.2 cutover window (all customers)

### Support Readiness
- Docs draft → ready (80%)
- FAQs in draft/ready (60%)
- Hotline staffed (40%)
- Training materials (in progress)

### Dependencies & Blockers
- VAT mapping override required
- Legacy data export dependency (NordForge)
- Training access fix (Helio)
- Feature A UAT verification (Meridian)
- Release engineering cutover

## Technology Stack
- Project Management: Milestone tracking, phase gates
- Customer Management: Rollout coordination, signoff workflow
- Readiness Assessment: Training, support, documentation
- Risk Management: Blocker tracking, dependency management
- Launch Coordination: Cutover planning, hypercare

## Getting Started
```bash
git clone https://github.com/ACME-Mock-EU/release-42-eu-onboarding.git
cd release-42-eu-onboarding
python main.py
```

## API Endpoints
- GET /customers - All 6 customers
- GET /customers/{name}/rollout - Customer rollout status
- GET /milestones - All 50 milestones
- GET /milestones/{id}/readiness - Milestone readiness
- POST /milestones/{id}/signoff - Customer signoff
- GET /blockers - Critical blockers
- GET /launch/confidence - Overall launch confidence
- GET /hypercare/plan - Post-launch hypercare plan

## Rollout Phases

**Planning (June 3-16):**
- VAT mapping workshop
- Legacy vendor export handoff
- Readiness: 56-74%

**UAT (June 12 - July 12):**
- UAT Kickoff
- Data Migration
- Feature A Go-Live
- UAT Exit gate
- Readiness: 70-93%
- Training: 44-96%

**Deployment (July 14):**
- Release 4.2 Cutover
- Merchant system cutover
- Infrastructure cutover
- Readiness: 83-84%

**Post-Launch (July 15+):**
- Hypercare (72h)
- Invoicing dry run
- Readiness: 87-91%

## Timeline
- June 3: Planning phase start (BluePeak)
- June 12: UAT kickoff (Meridian, UrbanNest)
- June 22: ClearWave UAT exit
- July 5: NordForge UAT exit
- July 10: Meridian Feature A go-live
- July 14: Release 4.2 cutover (all customers)
- July 15: Hypercare starts
- July 29: EOM invoicing dry run

## Roadmap
- v1.0: Release 4.2 launch (July 14)
- v1.1: Post-launch optimization
- v1.2: Hypercare wrap-up

## License
Internal use only - Acme Horizon Group

## Support
release-team@acmemock02.de | support@acmemock02.de
