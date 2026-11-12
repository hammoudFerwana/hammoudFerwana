<!-- ===================== HEADER ===================== -->
<div align="center">

<img src="assets/header.svg" width="100%" alt="Banner: Backend Engineer, Node.js, Express, MongoDB, PostgreSQL, Gaza, Palestine" />

# Mohammed Ferwana

<img src="assets/typing.svg" alt="I design secure, multi-tenant REST APIs. Sole backend engineer on Sawn, a claims SaaS. Clean layers, RBAC, state machines, tests." />

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

<!-- ===================== FEATURED ===================== -->
## Featured work

### Sawn

**Motor insurance claims SaaS.** B2B platform for insurance companies. A claim moves from first report to field inspection, review and final decision across a web dashboard and a Flutter field app. I am a co-founder and the sole backend engineer: API design, data model, tests and deployment.

<div align="center">
  <img src="assets/claim-lifecycle.svg" width="100%" alt="Sawn claim lifecycle state machine with 10 states" />
</div>

- Multi-tenant REST API on **Node.js, Express 5, MongoDB and Mongoose**, with Joi validation and JWT auth for three roles: Admin, Claims Officer and Field Adjuster.
- **10-state claim lifecycle** with role-guarded transitions and a full audit timeline for every status change.
- **Map-based dispatch:** adjusters ranked by distance to the accident, with a workload cap of 3 active claims. An officer override leaves an audit note.
- Evidence photos and digital signatures on **Cloudinary**, push notifications through **Firebase Cloud Messaging**, PDF claim reports.
- Public claim tracking link, coverage check at intake, loss assessment with deductible rules.
- **1248 automated tests across 63 suites** (full run, 11 Nov 2026). API deployed on Render, dashboard on Vercel. 4th place at Startup MVP Bootcamp.

<a href="https://insurflow-dashboard.vercel.app/"><img src="https://img.shields.io/badge/Open%20the%20live%20dashboard-22D3EE?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0D1117" alt="Open the Sawn live dashboard" /></a>
<a href="https://github.com/InsurFlow-Team/insurflow-backend"><img src="https://img.shields.io/badge/Backend%20source%20code-8B5CF6?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="Open the Sawn backend repository on GitHub" /></a>

### TeamLine

**Project management backend for small teams.** Built during the 144-hour TAQAT intensive training at Code Map. I was the backend developer and the team lead.

- REST API on **Node.js, Express and MongoDB**, with JWT authentication and bcrypt password hashing.
- Modules for workspaces, boards, tasks, time tracking, reports and a dashboard.
- Feature-based layout: each module has its own routes, controller, service and model.

<a href="https://team-line-frontend-eight.vercel.app/"><img src="https://img.shields.io/badge/Open%20the%20live%20app-22D3EE?style=for-the-badge&logo=vercel&logoColor=white&labelColor=0D1117" alt="Open the TeamLine live app" /></a>
<a href="https://github.com/Team-line/TeamLine-Backend"><img src="https://img.shields.io/badge/TeamLine%20backend%20source-8B5CF6?style=for-the-badge&logo=github&logoColor=white&labelColor=0D1117" alt="Open the TeamLine backend repository on GitHub" /></a>

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== HOW I BUILD ===================== -->
## How I build APIs

<div align="center">
  <img src="assets/request-pipeline.svg" width="100%" alt="A request moves through router, Joi validation, JWT and RBAC auth, controller, service and repository layers to MongoDB, and a JSON envelope returns" />
</div>

- **Layered modules.** Each feature has its own route, validator, controller, service, repository and model.
- **Multi-tenant by default.** `organizationId` comes from the JWT. Cross-tenant access returns `404`, so IDs leak nothing.
- **Race-safe state changes.** One atomic `findOneAndUpdate` checks tenant, expected status and owner in the same query.

<img src="assets/divider.svg" width="100%" height="8" alt="" />

<!-- ===================== EXPERIENCE ===================== -->
## Experience and more work

<details>
<summary><b>Experience and programs</b>: TAQAT · SAIOS Academy · GSG · Clinic Management System · Masar Tech · Areisto Software · IEEEXtreme</summary>
<br/>

| Where | Role | Highlights |
| :--- | :--- | :--- |
| **TAQAT** · TeamLine | Backend Developer and Team Lead | 144-hour intensive training at Code Map, 2026 |
| **SAIOS Academy** · SAIOS Technology | Backend Developer | Authentication audit and role-based access review on an LMS backend. |
| **GSG** · Market Ready Developer Program | Team Lead | Resume parsing and profile sync project with Simera. |
| **Clinic Management System** | Team Lead | Led a team of 5 on a single-clinic MVP in 22 days. Backend on Node.js, Express and PostgreSQL. Frontend on React. |
| **Masar Tech** | Assistant Trainer | Startup MVP Bootcamp 2, starting Nov 2026 |
| **Areisto Software** | Backend Developer Trainee | Khireej Qader Program |
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

<!-- ===================== FOOTER ===================== -->
<div align="center">

**Let's build something reliable.** See my [portfolio](https://mohammed-ferwana-portfolio.vercel.app/), or reach me on [LinkedIn](https://www.linkedin.com/in/mohammed-ferwana/) or at [mohammedferwana2@gmail.com](mailto:mohammedferwana2@gmail.com).

<img src="assets/footer.svg" width="100%" height="110" alt="" />

</div>
