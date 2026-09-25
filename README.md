# Mohammed Ferwana

<p align="left">
  <strong>Backend Software Engineer</strong> specializing in scalable Node.js/Express architectures, multi-tenant B2B systems, and robust database design across MongoDB and PostgreSQL.
</p>

<p align="left">
  <a href="https://www.linkedin.com/in/mohammed-ferwana/">
    <img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://github.com/hammoudFerwana">
    <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="mailto:ferwana.dev@gmail.com">
    <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email" />
  </a>
</p>

---

### 📌 About Me

- 🎓 **Final-year Software Engineering Student** at **Al-Azhar University, Gaza**, focused strictly on backend systems engineering.
- 🚀 **Backend Engineering Fellow** @ **Masar Tech Bootcamp (Batch 2)**, refining advanced distributed patterns, relational modeling, and system design.
- 🛠️ **Core Focus**: Designing resilient REST APIs, multi-tenant isolation, RBAC/ABAC authorization layers, and automated CI/CD deployment pipelines.
- 🤝 **Collaboration & Workflow**: Strong advocate of trunk-compatible feature branching, Conventional Commits, strict PR reviews, and automated testing gates.

---

### 🛠️ Tech Stack

#### Languages & Core Runtime
<p align="left">
  <img src="https://img.shields.io/badge/JavaScript_(ES6+)-F7DF1E?style=flat-square&logo=javascript&logoColor=black" alt="JavaScript" />
  <img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white" alt="TypeScript" />
  <img src="https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white" alt="Node.js" />
  <img src="https://img.shields.io/badge/SQL-CC292B?style=flat-square&logo=sqlite&logoColor=white" alt="SQL" />
</p>

#### Backend Architecture & Security
<p align="left">
  <img src="https://img.shields.io/badge/Express.js-000000?style=flat-square&logo=express&logoColor=white" alt="Express.js" />
  <img src="https://img.shields.io/badge/REST_API_Design-005571?style=flat-square&logo=postman&logoColor=white" alt="REST API" />
  <img src="https://img.shields.io/badge/JWT_Authentication-000000?style=flat-square&logo=jsonwebtokens&logoColor=white" alt="JWT" />
  <img src="https://img.shields.io/badge/RBAC_Authorization-4A154B?style=flat-square&logo=auth0&logoColor=white" alt="RBAC" />
  <img src="https://img.shields.io/badge/Multi--Tenancy-007ACC?style=flat-square&logo=blueprint&logoColor=white" alt="Multi-Tenancy" />
</p>

#### Databases & ORM / ODM
<p align="left">
  <img src="https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white" alt="MongoDB" />
  <img src="https://img.shields.io/badge/Mongoose-880000?style=flat-square&logo=mongoose&logoColor=white" alt="Mongoose" />
  <img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white" alt="PostgreSQL" />
  <img src="https://img.shields.io/badge/Sequelize_ORM-52B0E7?style=flat-square&logo=sequelize&logoColor=white" alt="Sequelize" />
</p>

#### DevOps, Testing & Tooling
<p align="left">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker" />
  <img src="https://img.shields.io/badge/CI%2FCD_Pipelines-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="CI/CD" />
  <img src="https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white" alt="GitHub Actions" />
  <img src="https://img.shields.io/badge/Jest_%26_Supertest-C21325?style=flat-square&logo=jest&logoColor=white" alt="Jest" />
  <img src="https://img.shields.io/badge/Postman-FF6C37?style=flat-square&logo=postman&logoColor=white" alt="Postman" />
  <img src="https://img.shields.io/badge/Git_%26_GitHub-F05032?style=flat-square&logo=git&logoColor=white" alt="Git" />
  <img src="https://img.shields.io/badge/Linux_CLI-FCC624?style=flat-square&logo=linux&logoColor=black" alt="Linux" />
</p>

---

### 💻 Featured Projects

#### 🏢 [InsurFlow — B2B SaaS Motor Insurance Claims Platform](https://github.com/InsurFlow-Team/insurflow-backend)
> **Role:** Backend Architect & Team Lead  
> **Problem & Solution:** Eliminates manual insurance claim settlement delays by orchestrating policy checks, multi-party assessment dispatching, and settlement lifecycles within an enterprise multi-tenant ecosystem.  
> **Core Architecture:**
> - Enforces tenant data isolation at the query layer (`tenantId`/`organizationId`).
> - Implements a deterministic finite state machine (Draft → Submitted → Under Review → Approved → Settled) with role-based transitions.
> - Structured 5-layer design (Route → Validator → Controller → Service → Model) backed by automated regression tests and CI/CD pipelines.  
> **Stack:** `Node.js` `Express.js` `MongoDB` `Mongoose` `JWT` `Docker` `GitHub Actions` `Jest`

---

#### ⏱️ [TeamFlow — Kanban & Time Tracking Backend for SMEs](https://github.com/hammoudFerwana)
> **Role:** Backend Developer  
> **Problem & Solution:** Solves productivity visibility and billable hour discrepancies for regional SMEs through localized project management and granular work session tracking.  
> **Core Architecture:**
> - Aggregation pipelines for member utilization rates, task throughput, and real-time project metrics.
> - Granular access control for Team Admins, Project Managers, and Members.  
> **Stack:** `Node.js` `Express.js` `MongoDB` `REST API` `JWT` `Mongoose`

---

#### 🛒 Multi-Vendor E-Commerce Marketplace API
> **Role:** Backend Developer  
> **Problem & Solution:** Prevents stock collisions and simplifies vendor payouts across distributed merchant storefronts via transactional ordering workflows.  
> **Core Architecture:**
> - Relational schema modeling in PostgreSQL utilizing Sequelize ORM with foreign key constraints and transactional integrity.
> - Isolated vendor product management, stock decrement locks, and order status lifecycle.  
> **Stack:** `Node.js` `Express.js` `PostgreSQL` `Sequelize` `REST API` `JWT`

---

#### 📚 Learning Platform RESTful API
> **Role:** Backend Developer  
> **Problem & Solution:** Powers digital curriculum delivery, student enrollment verification, and learning metrics with optimized query latency.  
> **Core Architecture:**
> - Multi-role auth supporting Instructors, Students, and Admins.
> - Deterministic query filtering, sorting, cursor pagination, and file attachment handling.  
> **Stack:** `Node.js` `Express.js` `MongoDB` `JWT` `Postman`

---

#### 🌿 Palestinian Center for Environmental Development (PCED) CMS Backend
> **Role:** Backend Developer  
> **Problem & Solution:** Powers public environmental data distribution, research paper dissemination, and multi-author editorial publishing.  
> **Core Architecture:**
> - Role-based content publication pipeline (Draft, Review, Published) with automated payload sanitization and asset handling.  
> **Stack:** `Node.js` `Express.js` `MongoDB` `REST API`

---

### ⚙️ Engineering Principles & Git Hygiene

I treat backend code as an evolving production asset:
- **Layered Clean Architecture:** Strict separation between HTTP concerns, domain business logic, data persistence, and input validation schemas.
- **Security-First Mindset:** Stateless JWT auth, secure HTTP-only refresh token rotation, strict Joi/Zod request payload sanitization, and OWASP API security guidelines.
- **Disciplined Version Control:** Feature branch isolation (`feat/`, `fix/`, `chore/`), Conventional Commits (`feat(claims): add audit trail logging`), pull request reviews, and issue linking.
- **Contract-First APIs:** Clean, predictable response envelopes (`{ success, data, error, meta }`) with exact HTTP status codes and Postman documentation.

---

### 📊 GitHub Activity & Stats

<p align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=hammoudFerwana&show_icons=true&theme=tokyonight&hide_border=true&count_private=true" alt="Mohammed Ferwana GitHub Stats" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=hammoudFerwana&layout=compact&theme=tokyonight&hide_border=true" alt="Top Languages" />
</p>

<p align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user=hammoudFerwana&theme=tokyonight&hide_border=true" alt="GitHub Streak" />
</p>

---

### 📬 Connect With Me

- **LinkedIn:** [linkedin.com/in/mohammed-ferwana](https://www.linkedin.com/in/mohammed-ferwana/)
- **GitHub:** [github.com/hammoudFerwana](https://github.com/hammoudFerwana)
- **Direct Email:** [ferwana.dev@gmail.com](mailto:ferwana.dev@gmail.com)
