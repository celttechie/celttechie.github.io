<div class="resume-header">
    <h1>Brian Jarrett</h1>
    <div class="subtitle">Staff Platform Engineer & Technical Leader | Systems SRE, Declarative Infrastructure & Federal Compliance</div>
    <div class="contact-info">
        <span>Grove, OK (Remote)</span>
        <span><a href="mailto:celttechie@gmail.com">celttechie@gmail.com</a></span>
        <span><a href="https://celttechie.github.io/">celttechie.github.io</a></span>
        <span><a href="https://www.linkedin.com/in/bjarrett">linkedin.com/in/bjarrett</a></span>
        <span>U.S. Citizen (Clearance Eligible)</span>
    </div>
</div>

## Professional Summary

**Staff Platform Engineer and Systems SRE** with nearly 30 years of broad technology, software engineering, and enterprise infrastructure leadership, including 7+ years as Cloud Engineering Technical Leader at Cisco supporting Webex FedRAMP platforms across **6,000+ nodes**. Directed enterprise **Log4j zero-day response** under HHS PMO governance, engineered custom Ansible/Python inspection tooling that uncovered nested vulnerabilities missed by commercial scanners, and defended the FedRAMP ATO. Architected an enterprise vulnerability data platform and pioneered SRE Error Budget scoring that **scaled monthly remediation throughput ~10x** and **eliminated >90% of overdue compliance backlogs**.

Rooted in first-principles systems discipline from a U.S. Air Force AWACS radar background, bridging bare-metal compute, VMware, OpenStack, and distributed storage fabrics with deterministic automation in **Python, Ansible, and Linux**. Actively engineering open-source cloud-native platforms, including Single-Node OpenShift (SNO), GPU-accelerated AI infrastructure (vLLM), tactical edge gateways, and air-gapped packaging. **U.S. Citizen eligible for immediate Secret / Top Secret clearance sponsorship.**

## Core Technical Competencies

* **Platform Operations & Systems Reliability:** Deterministic Infrastructure Automation (Operations-as-Code), Python/Ansible Workflows, First-Principles RCA, Multi-Tier Fault Isolation, HA Clustering, Custom Telemetry (Flask Consoles, Tableau, Nagios).
* **Software Engineering & Automation:** Python (Flask, Plotly Dash, FastAPI, Pandas, SQLAlchemy, RobotPy), PHP (Centre/SIS), Bash, Ansible, SaltStack, REST APIs (Jira, Qualys), ETL Pipelines.
* **Enterprise Infrastructure & Virtualization:** Cisco UCS Bare Metal & CIMC/LOM, Hypervisors (VMware vSphere/ESXi, KVM/Libvirt, Proxmox VE, XenServer), OpenStack (Nova, Heat), PXE Provisioning, Scheduler Latency Optimization.
* **Storage & Fabrics:** Distributed Block Storage (Ceph RBD, iSCSI), Ceph Snapshots, SAN Fabric Operations (Cisco MDS Fibre Channel zoning).
* **Federal Compliance & Zero Trust Security:** FedRAMP Moderate (ATO Governance), DISA STIG Hardening (XCCDF/XML), Enterprise Threat Remediation, FreeIPA (HA, HBAC), Linux Bastion Architecture.
* **Active Technical Research (Lab):** Cloud-Native Virtualization (KubeVirt, CDI PR #4340), Kubernetes Operators (Go / `controller-runtime`), Red Hat OpenShift (SNO 4.16+), Defense Unicorns Zarf & Lula (OSCAL cATO), OpenTofu.

## Technical Architecture & Open-Source Systems Projects

* **Cloud-Native VM Operator & Upstream CDI Contribution ([github.com/celttechie/uds-vm-operator](https://github.com/celttechie/uds-vm-operator)):** Authored upstream PR ([#4340](https://github.com/kubevirt/containerized-data-importer/pull/4340)) in CNCF `kubevirt/containerized-data-importer` adding cryptographic checksum validation for DataVolume uploads. Engineered an air-gap ready Kubernetes operator managing NIST 800-53 VMs on KubeVirt/CDI within Defense Unicorns UDS (Python `kopf` to Go `controller-runtime`) with automated Lula OSCAL continuous compliance.
* **Tactical Autonomous Edge Gateway ([github.com/celttechie/tactical-edge-gateway](https://github.com/celttechie/tactical-edge-gateway)):** Architected an async Python edge engine bridging robotic autonomy streams (MAVLink 2.0, ROS2/DDS) to military C2 platforms (TAK Server / CoT XML) over contested DDIL radio links, with SQLite WAL store-and-forward buffering, circuit breakers, rootless containers, Zarf packaging, and Lula OSCAL compliance.
* **Tactical SD-WAN & Containerized Network Dataplane ([github.com/celttechie/tactical-edge-sdn](https://github.com/celttechie/tactical-edge-sdn)):** Designed a containerized SD-WAN reference platform for DDIL maritime environments using FRRouting + WireGuard on K3s, an async Python policy/link-probing daemon with Netlink kernel route actuators, and automated DISA STIG compliance via Lula (OSCAL).
* **OpenShift SNO & Bare-Metal AI Infrastructure ([openshift-sno-lab](https://github.com/celttechie/openshift-sno-lab) / [openshift-ai-infrastructure](https://github.com/celttechie/openshift-ai-infrastructure)):** Built a declarative substrate deploying Single-Node OpenShift (SNO 4.16+) via OpenTofu on KVM/libvirt (NVMe direct I/O tuned for <10ms etcd fsync, 1GB HugePages), configuring PCIe VFIO GPU passthrough, NVIDIA GPU Operator (CDI), vLLM serving, and PCIe bus recovery runbooks.

## Professional Experience

### **Cisco Systems** | Cloud Engineering Technical Leader (Staff Platform / Systems SRE)
*Aug 2019 – July 2026 | Remote (USA)*

* **Enterprise Zero-Day Incident Response & Federal ATO Defense (Log4j / 6,000+ Nodes):** Maintained and defended the FedRAMP ATO under HHS PMO governance across 6,000+ operational bare-metal and cloud systems during the enterprise Log4j zero-day crisis. Engineered custom Ansible inspection playbooks and Python tooling to rapidly identify nested and shaded Java libraries missed by commercial scanners, delivered actionable remediation datasets to engineering teams, verified remediation, and compiled technical evidence packages validating compliance under strict federal deadlines.
* **Vulnerability Governance Platform & SRE Error Budget Architecture (Flask, PostgreSQL, Tableau):** Scaled monthly remediation throughput ~10x, cut High-severity remediation time >40%, and drove overdue backlogs down >90% across 6,000+ systems by architecting a FedRAMP governance platform (Python Flask, Plotly Dash, SQLAlchemy, TabPy). Pioneered SRE "Error Budget" mathematical algorithms (Severity × Blast Radius × Time Decay) with automated variance credits, dynamic Ansible inventory patching, and executive scorecards.
* **FedRAMP Continuous Monitoring (ConMon) Inventory Reconciliation:** Eliminated 12–15 hours of monthly manual "stare and compare" audits across SecOps by engineering Python/Pandas automation reconciling 80,000-record ConMon inventories against ServiceNow CMDB and Qualys APIs, eliminating human error.
* **Cross-Discipline Systems Translation & Root Cause Analysis (RCA):** Accelerated remediation velocity across software, storage, and networking teams by translating complex CVEs, kernel vulnerabilities, and DISA STIGs into actionable remediation paths, authoring formal compliance deviation packages for the federal PMO.
* **Compliance-as-Code & SRE Toil Elimination (STIG XCCDF/XML & Qualys API):** Eliminated hundreds of engineering hours of manual compliance auditing by building automated Python pipelines that ingested Qualys API results, parsed DISA STIG XCCDF (XML) benchmarks, and correlated running Linux server configurations directly to federal controls.
* **Engineering Mentorship & Operational Handover:** Accelerated team autonomy during engineer onboarding by walking new engineers through the underlying systems and custom monthly compliance automation scripts in the first cycle, then verifying their execution as they ran the workflows in the next cycle before transitioning full operational ownership.

### **Cisco Systems** | Cloud Systems Engineer & Lead Compute Engineer (Senior SRE / Infrastructure)
*Jan 2017 – Aug 2019 | Remote (USA)*

* **Lead Compute Engineering, Virtualization & SAN Fabric Operations:** Upheld continuous federal SLA compliance and high availability across enterprise VMware vSphere clusters and Cisco UCS bare metal, executing rolling zero-downtime ESXi upgrades and reconfiguring Cisco MDS Fibre Channel SAN zoning to expand enterprise capacity.
* **Compute Security, Package Repository Governance & Automated Patching:** Transitioned reactive vulnerability tracking into a proactive engineering pipeline using Python REST ETL and dynamic Ansible inventory automation, while maintaining internal package repositories inside the FedRAMP boundary to replace unvalidated custom Puppet packages with chain-of-custody validated updates.
* **High-Availability Enterprise Identity & SOC Collaboration (FreeIPA/HBAC):** Architected and deployed an automated, high-availability FreeIPA cluster in OpenStack using Ansible to replace a legacy 389 Directory Server environment. Partnered with the Security Operations Center (SOC) to establish fine-grained Host-Based Access Control (HBAC) rule sets and advised application teams on service permissions across 2,000+ hosts.
* **FedRAMP Audit Defense & Automated Evidence Collection:** Defended federal secure access controls across multiple annual FedRAMP audits, serving as primary engineering SME for bastion jump hosts, Active Directory domain controllers, and LDAP/FreeIPA identity platforms. Authored custom Ansible playbooks and shell scripts to automate evidence gathering across 2,000+ systems, eliminating manual console audit toil.

### **Select Group @ Cisco** | Cloud DevOps/QA Engineer (Cloud Systems SRE)
*Feb 2016 – Jan 2017 | Remote (USA)*

* **Scheduler Latency Optimization & Cloud Orchestration (OpenStack Nova):** Eliminated cloud provisioning bottlenecks by identifying and removing redundant Nova Scheduler filters in OpenStack for Cisco's InterCloud Services (OpenStack-on-OpenStack on Cisco UCS bare metal), reducing instance scheduling time for 700 nodes from 20 seconds to 5 seconds—a **75% improvement** in orchestration speed.
* **Bare-Metal Provisioning, Infrastructure as Code & Platform Evaluation:** Engineered automated bare-metal PXE boot and Ansible provisioning workflows via lights-out management (LOM) interfaces across hundreds of production Cisco UCS servers in Cisco InterCloud Services, and conducted proof-of-concept (PoC) evaluations of local Red Hat Update Infrastructure (RHUI) repositories and Proxmox hypervisor clusters.
* **Cloud Stability Engineering & Windows Provisioning RCA (cloudbase-init):** Eliminated persistent deployment failures and reboot loops on Windows Server instances in OpenStack by diagnosing a race condition between Sysprep specialize and cloudbase-init, configuring SetupComplete.cmd to achieve 100% reliable first-boot provisioning.
* **Blue/Green Upgrade Verification & Cloud Orchestration QA:** Guaranteed zero-downtime production cutovers for major OpenStack-on-OpenStack blue/green upgrades as the final verification gate, building automated Python, Bash, and Ansible test suites for Nova Compute and Heat to intercept regressions before traffic migration.

### **Australian Laboratory Services** | Senior Systems & Storage Administrator
*Sep 2014 – Jan 2016 | Grand Junction, CO*

* **Distributed Storage Engineering (Ceph RBD & VMware ESXi):** Engineered an Ubuntu Ceph cluster for VMware ESXi hosts, benchmarking iSCSI vs. RBD performance and leveraging Ceph RBD snapshots for automated database schema testing, enabling a zero-error production upgrade.
* **Resilient Storage & Automated Provisioning (Ceph / SaltStack):** Architected a high-availability Ceph + SaltStack platform on commodity Dell servers; proved 2-of-3 node fault tolerance in a live executive demo with uninterrupted data access.
* **System Telemetry & Network Reliability:** Integrated Nagios/Observium telemetry reducing service restarts from weekly to quarterly, and upgraded gateway hardware to double WAN/VPN throughput.

### **Foundational Systems, Software & QA Experience** | Garfield County SD 16 · Glenn Abbey Software · StorageSoft
*Sep 1997 – Jun 2014 | Colorado & Remote*

* **Software Engineering & Commercial SIS (`2002–2014`):** Built a **Python (Flask/SQLAlchemy)** SIS-to-AD/Google Apps sync app cutting account support calls **97%**. Contracted by **Glenn Abbey Software (`2006–2014`)** for core **PHP** development on **Centre/SIS** across multiple states—redesigning grading/GPA (`CalcGPA.php`) and transcripts, automating Colorado ("October Count") and Arkansas (**APSCN** via **Python**) reporting, and centralizing **PostgreSQL** databases.
* **Virtualization & Infrastructure (`2002–2014`):** Consolidated servers onto **Citrix XenServer** with local building AD domain controllers; engineered a **100+ Mbps Ruckus wireless WAN** (**+6,500%** bandwidth, $0 monthly cost), Cisco VoIP, and thin-client labs (**$60K+ CAPEX saved**).
* **Pre-Sysprep Disk Cloning & QA (`1997–2002`):** QA Lead, Technical Services Manager, and Sales Engineer for **ImageCast IC3** & **DrivePro**. Solved duplicate Windows NT **Machine SIDs** in the registry before Microsoft Sysprep existed; built multi-OS PXE/multicast test labs and validated Microsoft SMS / CA Unicenter integrations for HP, Target, and NEC.

## Systems Leadership & Robotics Mentorship

### **FIRST Robotics Team 3160 (F.R.O.G.)** | Lead Engineering & Systems Mentor *(2016 – Present)*

* **Real-Time Control Systems & Telemetry:** Mentored students and developed Python (RobotPy) software for real-time control loops, swerve drive kinematics, CAN bus telemetry, sensor fusion, and AprilTags computer vision.
* **Subsystem Testing & Motor Simulation (`FROGlib` / Phoenix 6):** Built automated tests and integrated CTRE Phoenix 6 motor controller simulation into `FROGlib` to validate mechanisms before hardware deployment; diagnosed mechanical/electrical/sensor failures under tournament constraints.

## Military Service, Clearance & Education

* **Avionics Specialist – AWACS RADAR** | **United States Air Force** *(Jul 1991 – Jul 1995 | Tinker AFB, OK)*: Guaranteed flightline mission readiness for E-3 Sentry (AWACS) radar systems across high-power microwave transmitters and digital signal processors. **Honor Graduate (99% average)**; **Senior Airman Below-the-Zone (BTZ)**. Honorable Discharge.
* **Security Clearance & Education:** U.S. Citizen eligible for immediate Secret / Top Secret clearance sponsorship (FedRAMP Moderate / DISA STIG background). Engineering Coursework, Colorado School of Mines; ongoing specialization in Kubernetes/OpenShift, AI infrastructure, and IaC (OpenTofu, Ansible).
