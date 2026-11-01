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

Platform Engineering Technical Leader and Systems SRE with 15+ years of enterprise platform leadership spanning bare-metal compute, Linux systems administration, enterprise virtualization, and Site Reliability Engineering (SRE)—including 7+ years of technical leadership at Cisco in the Webex FedRAMP environment on Cisco UCS, VMware, and OpenStack platforms. A methodical problem-solver who approaches infrastructure from first principles, favoring deterministic, declarative automation to eliminate repetitive operational toil, ensuring secure, high-uptime platform operations across 6,000+ production systems.

U.S. Air Force veteran actively engineering open-source defense and cloud-native reference platforms—spanning tactical telemetry gateways (MAVLink/ROS2 to TAK/CoT), containerized SD-WAN dataplanes on K3s, accelerated AI infrastructure (PCIe VFIO GPU passthrough, NVIDIA GPU Operator, vLLM), and Single-Node OpenShift (SNO 4.16+). Combines deep root-cause diagnostic mastery spanning the full stack—from physical compute, hypervisors, and SAN storage fabrics up to Kubernetes container platforms and zero-trust access control—with proven automation in Python, Ansible, and Bash. U.S. Citizen eligible for immediate Secret / Top Secret security clearance sponsorship.

## Core Technical Competencies

* **Platform Operations & Systems Reliability:** Deterministic Infrastructure Automation (Shifting Operations to Code), Automated Repeatable Workflows (Python, Ansible), First-Principles Root Cause Analysis (RCA), Multi-Tier Fault Isolation (Hardware, Kernel, OS & Service Logs), High Availability (HA) Clustering, Custom Observability & Telemetry (Vulnerability Aggregation Pipelines, Python/SQLAlchemy Consoles, Tableau SLA Dashboards, Nagios).
* **Python Engineering & Systems Automation:** Python (FastAPI, Pandas, SQLAlchemy, Flask, RobotPy), Bash / Shell Scripting, Ansible Playbooks & Roles, SaltStack, REST APIs (Jira, Qualys), Custom Systems Automation & ETL Pipelines.
* **Enterprise Infrastructure & Virtualization:** Cisco UCS Bare Metal & CIMC/LOM, Enterprise Hypervisors (VMware vSphere/ESXi, KVM/Libvirt, Proxmox VE), OpenStack (Nova, Heat), Bare-Metal PXE Boot Provisioning, Compute Scheduler Latency Optimization.
* **Storage Systems & Fabrics:** Distributed Block Storage (Ceph RBD, iSCSI), Ceph Snapshots, SAN Fabric Operations (Cisco MDS Fibre Channel switches and zoning).
* **Federal Compliance & Zero Trust Security:** FedRAMP Moderate Operations (Federal ATO Governance), DISA STIG Hardening (XCCDF/XML parsing), Rapid Threat Assessment & Enterprise-Wide Remediation, FreeIPA (HA, Host-Based Access Control - HBAC), Linux Bastion Architecture.
* **Active Technical Research (Lab):** Red Hat OpenShift (SNO 4.16+), Kubernetes (K3s, RKE2), Container Runtimes (Docker, Podman, CRI-O), Infrastructure as Code (OpenTofu), Defense Unicorns Zarf & Lula (OSCAL v1.1.2 Automated Compliance), Air-Gapped / Disconnected Delivery.

## Technical Architecture & Open-Source Systems Projects

* **Tactical Autonomous Edge Gateway ([github.com/celttechie/tactical-edge-gateway](https://github.com/celttechie/tactical-edge-gateway)):** Architected an asynchronous Python edge engine bridging heterogeneous robotic autonomy streams (MAVLink 2.0, ROS2/DDS) to military C2 situational awareness platforms (TAK Server / Cursor on Target XML) over contested, disconnected (DIL) tactical radio links. Designed local SQLite WAL store-and-forward buffering with circuit breakers, rootless container security, air-gapped Zarf packaging, Lula OSCAL continuous compliance validation, and formalized system architecture across 10 Architecture Decision Records (ADRs).
* **Tactical SD-WAN & Containerized Network Dataplane ([github.com/celttechie/tactical-edge-sdn](https://github.com/celttechie/tactical-edge-sdn)):** Designed a cloud-native, containerized Software-Defined Networking (SD-WAN) reference platform modernizing legacy shipboard network routing (ADNS/CANES baselines) for DDIL maritime environments. Engineered a containerized FRRouting + WireGuard dataplane on K3s, an asynchronous Python policy and link-probing daemon with Netlink actuators, and automated DISA STIG compliance via Lula (OSCAL), validated across a Dell Precision T5600 Libvirt hypervisor with pre-configured support for low-SWaP ARM64 tactical hardware.
* **Accelerated AI Infrastructure & Model Serving ([github.com/celttechie/openshift-ai-infrastructure](https://github.com/celttechie/openshift-ai-infrastructure)):** Built a bare-metal accelerated computing testbed configuring host PCIe VFIO driver binding and IOMMU group isolation using a custom Python state machine (`gpu-host-admin.py`). Deployed the NVIDIA GPU Operator with CRI-O Container Device Interface (CDI) and time-slicing; benchmarked continuous batching and PagedAttention in vLLM; authored SRE operational runbooks for PCIe bus recovery and kernel post-mortems.
* **Declarative OpenShift SNO Platform Substrate ([github.com/celttechie/openshift-sno-lab](https://github.com/celttechie/openshift-sno-lab)):** Automated Single-Node OpenShift (SNO 4.16+) platform deployment on headless KVM/Libvirt via OpenTofu, strictly decoupling infrastructure provisioning from workload lifecycles. Tuned NVMe storage pools (`cache=none`, `io=threads`) to achieve sub-10ms `etcd` fsync latency, configured RHCOS MachineConfigs for boot-time 1GB HugePages, and enforced zero-trust access via native OpenTofu Ed25519 key generation.

## Professional Experience

### **Cisco Systems** | Cloud Engineering Technical Leader (Staff Platform / Systems SRE)
*Aug 2019 – July 2026 | Remote (USA)*

* **Enterprise Zero-Day Incident Response & Federal ATO Defense (Log4j / 6,000+ Nodes):** Defended continuous FedRAMP ATO under HHS PMO governance across 6,000+ operational bare-metal and cloud systems during the enterprise Log4j zero-day crisis. Engineered custom Ansible inspection playbooks and Python tooling to rapidly identify nested and shaded Java libraries missed by commercial scanners, delivered actionable remediation datasets to engineering teams and directors, verified remediation, and compiled technical evidence packages validating compliance under strict federal deadlines.
* **Vulnerability Governance Platform & SRE Error Budget Architecture (Python, PostgreSQL, Tableau):** Scaled monthly remediation throughput ~10x, cut High-severity remediation time >40%, and drove overdue backlogs down >90% across 6,000+ systems by architecting a FedRAMP governance platform. Pioneered SRE "Error Budget" mathematical algorithms (Severity × Blast Radius × Time Decay) with automated variance credits, dynamic Ansible inventory patching, and executive scorecards.
* **FedRAMP Continuous Monitoring (ConMon) Inventory Reconciliation:** Eliminated 12–15 hours of monthly manual "stare and compare" audits across the SecOps team by engineering Python and Pandas automation reconciling 80,000-record ConMon inventories against ServiceNow CMDB and Qualys APIs, eliminating human error and manual editing inconsistencies.
* **Cross-Discipline Systems Translation & Root Cause Analysis (RCA):** Accelerated remediation velocity and eliminated cross-team blockers by translating complex CVEs, kernel vulnerabilities, and DISA STIG benchmarks into actionable remediation paths for software, storage, and networking teams. Conducted root-cause analysis (RCA) and authored formal compliance deviation packages submitted to the federal PMO.
* **Compliance-as-Code & SRE Toil Elimination (STIG XCCDF/XML & Qualys API):** Eliminated hundreds of engineering hours of manual compliance auditing by building automated Python pipelines that ingested Qualys API results, parsed DISA STIG XCCDF (XML) benchmarks, and correlated running Linux server configurations directly to federal controls.
* **Engineering Mentorship & Structured Operational Handover:** Accelerated team autonomy by instituting a two-phase onboarding model: teaching underlying system mechanics, training on custom automation tooling, and co-piloting live recurring workflows in Month 1 to transition full operational ownership by Month 2 under federal SLAs.

### **Cisco Systems** | Cloud Systems Engineer & Lead Compute Engineer (Senior SRE / Infrastructure)
*Jan 2017 – Aug 2019 | Remote (USA)*

* **Lead Compute Engineering, Virtualization & SAN Fabric Operations:** Maintained high availability and strict federal SLAs across enterprise VMware vSphere clusters and Cisco UCS bare metal, resolving virtualization performance bottlenecks and supporting Cisco MDS Fibre Channel SAN switch fabrics and zoning.
* **High-Availability Enterprise Identity & SOC Collaboration (FreeIPA/HBAC):** Architected and deployed an automated, high-availability FreeIPA cluster in OpenStack using Ansible to replace a legacy 389 Directory Server environment. Partnered with the Security Operations Center (SOC) to establish fine-grained Host-Based Access Control (HBAC) rule sets, standardizing zero-trust identity across 2,000+ hosts.
* **FedRAMP Audit Defense & Automated Evidence Collection:** Defended federal secure access controls across multiple annual FedRAMP audits, serving as primary engineering SME for bastion jump hosts, Active Directory domain controllers, and LDAP/FreeIPA identity platforms. Authored custom Ansible playbooks and shell scripts to automate evidence gathering across 2,000+ systems, eliminating manual console audit toil.

### **Select Group @ Cisco** | Cloud DevOps/QA Engineer (Cloud Systems SRE)
*Feb 2016 – Jan 2017 | Remote (USA)*

* **Scheduler Latency Optimization & Cloud Orchestration (OpenStack Nova):** Eliminated cloud provisioning bottlenecks by identifying and removing redundant Nova Scheduler filters in OpenStack for Cisco's InterCloud Services (OpenStack-on-OpenStack on Cisco UCS bare metal), reducing instance scheduling time for 700 nodes from 20 seconds to 5 seconds—a **75% improvement** in orchestration speed.
* **Bare-Metal Provisioning, Infrastructure as Code & Platform Evaluation:** Eliminated repetitive manual deployment toil by engineering automated bare-metal PXE boot and Ansible provisioning workflows across hundreds of production Cisco UCS servers in Cisco InterCloud Services. Automated ongoing configuration baselines via lights-out management (LOM) interfaces, and evaluated next-generation platform substrates—prototyping local Red Hat Update Infrastructure (RHUI) for secure, zero-egress internal package distribution and benchmarking Proxmox hypervisor clusters.
* **Cloud Stability Engineering & Windows Provisioning RCA (cloudbase-init):** Eliminated persistent deployment failures and infinite reboot loops across Windows Server cloud instances by diagnosing a complex race condition between Sysprep specialize and cloudbase-init in OpenStack, implementing the fix to achieve 100% reliable first-boot provisioning.
* **Blue/Green Upgrade Verification & Cloud Orchestration QA:** Served as the final verification gate for major OpenStack-on-OpenStack blue/green upgrades, building automated Python, Bash, and Ansible test suites for Nova Compute and Heat to catch regressions and guarantee zero-downtime production cutovers.

### **Australian Laboratory Services** | Senior Systems & Storage Administrator
*Sep 2014 – Jan 2016 | Grand Junction, CO*

* **Distributed Storage Engineering (Ceph RBD & VMware ESXi):** Engineered an Ubuntu-based Ceph cluster for VMware ESXi hosts, benchmarking iSCSI vs. RBD performance to optimize block storage access. Leveraged Ceph RBD snapshots to manage automated database schema testing, enabling a major production database upgrade with zero errors.
* **Resilient Storage Architecture & Automated Provisioning (Ceph / SaltStack):** Architected a cost-effective high-availability storage and compute platform across commodity Dell rackmount servers, using Ceph distributed block storage to protect virtual machine disks against physical host failures. Validated fault tolerance in an executive demonstration by maintaining uninterrupted data access while systematically failing two of three storage nodes; leveraged SaltStack to automate rapid VM provisioning and cluster configuration.
* **System Telemetry & Network Reliability:** Integrated proactive telemetry checks into Nagios and Observium to monitor production systems, decreasing service restarts from weekly to quarterly. Diagnosed WAN/VPN bottlenecks and upgraded gateway hardware to double network throughput.

### **Foundational Systems, Infrastructure & Testing Experience**
*Prior Systems Foundations (StorageSoft / Phoenix Technologies)*

* **Engineering Operations & Greenfield Lab Buildout:** Built out corporate server and network infrastructure from scratch following a spin-off. Reorganized QA and support into a 10-person rotating team: technicians alternated between hands-on lab validation (drive controllers, NICs, PXE boot, multicast routing) and customer support, enabling direct lab reproduction of field issues and accelerating resolution times.
* **Quality Engineering Foundations & Defect Governance:** Promoted from contractor to QA Lead, transforming ad-hoc testing into a standardized quality engineering lifecycle. Replaced informal email chains and handwritten notepads with the company's first centralized bug-tracking system and structured multi-OS test matrices, eliminating defect escapes in commercial releases.

## Systems Leadership & Robotics Mentorship

### **FIRST Robotics Team 3160 (F.R.O.G.)** | Lead Engineering & Systems Mentor
*2014 – Present (10+ Years)*

* **Real-Time Control Systems & Telemetry:** Mentored high school engineering students and developed Python (RobotPy) software for real-time robot control loops, swerve drive kinematics, distributed CAN bus telemetry, sensor fusion, and AprilTags computer vision.
* **Subsystem Testing & Physics Simulation:** Built automated testing routines and physics simulations to validate robot mechanisms and drive code prior to hardware deployment; diagnosed critical mechanical, electrical, and sensor failures under intense tournament constraints.

## Military Service, Clearance & Education

* **Airborne Warning and Control Radar Journeyman (AWACS)** | **United States Air Force**  
  *Directly guaranteed operational mission readiness for E-3 Sentry (AWACS) radar platforms on the flightline. Debriefed aircrew and conducted precision repairs across high-power microwave transmitters, high-voltage power supplies, and digital signal processors under strict operational turn-around deadlines. Honorable Discharge.*
* **Security Clearance Status:** U.S. Citizen eligible for immediate Secret / Top Secret security clearance sponsorship; extensive career background operating within FedRAMP Moderate (HHS PMO ATO) and DISA STIG compliance boundaries.
* **Education & Continuous Learning:** Engineering Coursework, Colorado School of Mines. Ongoing technical specialization in Kubernetes/OpenShift container platforms, accelerated AI infrastructure, Infrastructure as Code (OpenTofu, Ansible), and Federal Zero-Trust Architectures.
