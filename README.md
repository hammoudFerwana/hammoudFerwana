<!-- ===================== HEADER ===================== -->
<div align="center">

<img src="assets/header.svg" width="100%" alt="Banner: Backend Engineer, Node.js, Express, MongoDB, PostgreSQL, Gaza, Palestine" />

# Mohammed Ferwana

<img src="assets/typing.svg" alt="I design secure, multi-tenant REST APIs. Sole backend engineer on Sawn, a claims SaaS. Clean layers, RBAC, state machines, tests." />

<a href="https://www.linkedin.com/in/mohammed-ferwana/"><img src="https://img.shields.io/badge/LinkedIn-mohammed--ferwana-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0D1117" alt="LinkedIn profile" /></a>
<a href="mailto:mohammedferwana2@gmail.com"><img src="https://img.shields.io/badge/Email-mohammedferwana2%40gmail.com-8B5CF6?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0D1117" alt="Email mohammedferwana2@gmail.com" /></a>
<a href="https://insurflow-dashboard.vercel.app/"><img src="https://img.shields.io/badge/Sawn-Live%20dashboard-22D3EE?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0D1117" alt="Sawn live dashboard" /></a>

**Sole backend engineer on Sawn** · 387 automated tests · 10-state claim lifecycle · API live on Render

<a href="mailto:mohammedferwana2@gmail.com?subject=Backend%20role%20or%20freelance%20API%20work"><img src="https://img.shields.io/badge/Open%20to-remote%20backend%20roles%20%C2%B7%20freelance%20API%20work-3FB950?style=for-the-badge&labelColor=0D1117" alt="Open to remote backend roles and freelance API work" /></a>

</div>

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== ABOUT ===================== -->
## About me

<div align="center">
  <img src="assets/terminal.svg" width="100%" alt="Terminal calling GET /api/v1/me and printing Mohammed's profile as JSON" />
</div>

<br/>

I build the server side of products: APIs, data models, authentication and the business rules between them. My main stack is **Node.js, Express and MongoDB**, and I am adding **PostgreSQL** to my daily work. I study **Computer Systems Engineering at Al-Azhar University, Gaza** (class of 2027, CGPA 93.3).

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== FEATURED ===================== -->
## Featured work: Sawn

**Motor insurance claims SaaS.** B2B platform for insurance companies. A claim moves from first report to field inspection, review and final decision across a web dashboard and a Flutter field app. I own the backend: API design, data model, tests and deployment.

<div align="center">
  <img src="assets/claim-lifecycle.svg" width="100%" alt="Sawn claim lifecycle state machine with 10 states" />
</div>

- Multi-tenant REST API on **Node.js, Express 5, MongoDB and Mongoose**, with Joi validation and JWT auth for three roles: Admin, Claims Officer and Field Adjuster.
- **10-state claim lifecycle** with role-guarded transitions and a full audit timeline for every status change.
- **Map-based dispatch:** adjusters ranked by distance to the accident, with a workload cap of 3 active claims. An officer override leaves an audit note.
- Evidence photos and digital signatures on **Cloudinary**, push notifications through **Firebase Cloud Messaging**, PDF claim reports.
- Public claim tracking link, coverage check at intake, loss assessment with deductible rules.
- **387 automated tests across 27 suites.** API deployed on Render, dashboard on Vercel. 4th place at Startup MVP Bootcamp.

<a href="https://insurflow-dashboard.vercel.app/"><img src="https://img.shields.io/badge/Open%20the%20live%20dashboard-22D3EE?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0D1117" alt="Open the Sawn live dashboard" /></a>
<img src="https://img.shields.io/badge/Backend%20source-private-30363D?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="Backend source is private" />

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== HOW I BUILD ===================== -->
## How I build APIs

<div align="center">
  <img src="assets/request-pipeline.svg" width="100%" alt="A request moves through router, Joi validation, JWT and RBAC auth, controller, service and repository layers to MongoDB, and a JSON envelope returns" />
</div>

- **Layered modules.** Each feature has its own route, validator, controller, service, repository and model.
- **Multi-tenant by default.** `organizationId` comes from the JWT. Cross-tenant access returns `404`, so IDs leak nothing.
- **Race-safe state changes.** One atomic `findOneAndUpdate` checks tenant, expected status and owner in the same query.
- **Predictable contracts.** One response envelope `{ success, data, error, meta }`, camelCase everywhere, exact HTTP status codes.
- **Proof before merge.** Automated tests per feature, feature branches, Conventional Commits and reviewed pull requests.

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== STACK ===================== -->
## Tech stack

<table>
  <tr>
    <td align="center" width="170"><b>Languages</b></td>
    <td><img src="https://skillicons.dev/icons?i=js,ts,html,css&theme=dark" alt="JavaScript, TypeScript, HTML, CSS" /></td>
  </tr>
  <tr>
    <td align="center"><b>Backend</b></td>
    <td><img src="https://skillicons.dev/icons?i=nodejs,express&theme=dark" alt="Node.js, Express" /></td>
  </tr>
  <tr>
    <td align="center"><b>Databases</b></td>
    <td><img src="https://skillicons.dev/icons?i=mongodb,postgres,sequelize&theme=dark" alt="MongoDB, PostgreSQL, Sequelize" /></td>
  </tr>
  <tr>
    <td align="center"><b>DevOps and testing</b></td>
    <td><img src="https://skillicons.dev/icons?i=docker,githubactions,jest,linux,bash&theme=dark" alt="Docker, GitHub Actions, Jest, Linux, Bash" /></td>
  </tr>
  <tr>
    <td align="center"><b>Tools</b></td>
    <td><img src="https://skillicons.dev/icons?i=git,github,postman,vscode,firebase,vercel&theme=dark" alt="Git, GitHub, Postman, VS Code, Firebase, Vercel" /></td>
  </tr>
</table>

**Libraries and services I ship with**

![Mongoose](https://img.shields.io/badge/Mongoose-880000?style=flat-square&logo=mongoose&logoColor=white)
![Joi](https://img.shields.io/badge/Joi-validation-8B5CF6?style=flat-square&labelColor=0D1117)
![JWT](https://img.shields.io/badge/JWT-000000?style=flat-square&logo=jsonwebtokens&logoColor=white)
![bcrypt](https://img.shields.io/badge/bcrypt-hashing-8B5CF6?style=flat-square&labelColor=0D1117)
![Helmet](https://img.shields.io/badge/Helmet-security%20headers-8B5CF6?style=flat-square&labelColor=0D1117)
![MongoDB Atlas](https://img.shields.io/badge/MongoDB%20Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)
![Cloudinary](https://img.shields.io/badge/Cloudinary-3448C5?style=flat-square&logo=cloudinary&logoColor=white)
![Firebase Cloud Messaging](https://img.shields.io/badge/Firebase%20Cloud%20Messaging-DD2C00?style=flat-square&logo=firebase&logoColor=white)
![Render](https://img.shields.io/badge/Render-000000?style=flat-square&logo=render&logoColor=white)
![Trello](https://img.shields.io/badge/Trello-0052CC?style=flat-square&logo=trello&logoColor=white)

**AI-assisted workflow:** I plan and review with Claude and build with Google Antigravity. No change reaches `main` without a real diff and real test output.

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== REPOSITORIES ===================== -->
## Public repositories

<div align="center">
  <a href="https://github.com/hammoudFerwana/project-management-backend"><img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/pin-project-management-backend.svg" width="49%" alt="project-management-backend repository" /></a>
  <a href="https://github.com/hammoudFerwana/tour-booking-application"><img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/pin-tour-booking-application.svg" width="49%" alt="tour-booking-application repository" /></a>
  <a href="https://github.com/hammoudFerwana/subscription-tracker"><img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/pin-subscription-tracker.svg" width="49%" alt="subscription-tracker repository" /></a>
  <a href="https://github.com/hammoudFerwana/mohammed-ferwana-portfolio"><img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/pin-mohammed-ferwana-portfolio.svg" width="49%" alt="mohammed-ferwana-portfolio repository" /></a>
</div>

<!-- ===================== EXPERIENCE ===================== -->
## Experience and more work

<details>
<summary><b>Experience and programs</b>: Sawn · TAQAT · SAIOS Academy · GSG · Masar Tech · Areisto Software · IEEEXtreme</summary>
<br/>

| Where | Role | Highlights |
| :--- | :--- | :--- |
| **Sawn** (formerly InsurFlow) | Backend Engineer | Owns the full backend of a B2B claims SaaS. 4th place at Startup MVP Bootcamp. |
| **TAQAT** · TeamLine | Backend Developer and Team Lead | 2026 |
| **SAIOS Academy** · SAIOS Technology | Backend Developer | Authentication audit and role-based access review on an LMS backend. |
| **GSG** · Market Ready Developer Program | Team Lead | Resume parsing and profile sync project with Simera. |
| **Masar Tech** | Backend Engineering Bootcamp | Batch 2 |
| **Areisto Software** | Intern | Khireej Qader Program |
| **IEEEXtreme 20.0** | Competitor | 24-hour global programming contest, October 2026 |

</details>

<details>
<summary><b>Client and private work</b>: PCED CMS · Learning Platform API</summary>
<br/>

| Project | What I built | Stack |
| :--- | :--- | :--- |
| **PCED CMS** | Backend for the bilingual (Arabic and English) website of the Palestinian Center for Environmental Development | Node.js, Express, MongoDB, ES Modules |
| **Learning Platform API** | REST API for a learning platform, built on a layered architecture with dependency injection | Node.js, Express |

</details>

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== ACTIVITY ===================== -->
## GitHub activity

<div align="center">
  <img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/stats.svg" width="49%" alt="GitHub stats for hammoudFerwana" />
  <img src="https://streak-stats.demolab.com/?user=hammoudFerwana&background=0D1117&border=30363D&stroke=30363D&ring=8B5CF6&fire=22D3EE&currStreakNum=A78BFA&sideNums=E6EDF3&currStreakLabel=A78BFA&sideLabels=8B949E&dates=8B949E&border_radius=14" width="49%" alt="GitHub contribution streak" />
</div>

<br/>

<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/snake-dark.svg" />
    <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/snake-light.svg" />
    <img src="https://raw.githubusercontent.com/hammoudFerwana/hammoudFerwana/output/snake-dark.svg" width="100%" alt="Snake eating the contribution graph" />
  </picture>
</div>

<!-- ===================== FOOTER ===================== -->
<div align="center">

**Let's build something reliable.** Reach me on [LinkedIn](https://www.linkedin.com/in/mohammed-ferwana/) or at [mohammedferwana2@gmail.com](mailto:mohammedferwana2@gmail.com).

<img src="assets/footer.svg" width="100%" height="110" alt="" />

</div>
