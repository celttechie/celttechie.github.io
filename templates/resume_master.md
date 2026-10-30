<div class="resume-header">
    <h1>Brian Jarrett</h1>
    <div class="subtitle">Staff DevOps & Platform Engineer | Enterprise Infrastructure, Python & Federal Systems</div>
    <div class="contact-info">
        <span>Grove, OK (Remote)</span>
        <span><a href="mailto:celttechie@gmail.com">celttechie@gmail.com</a></span>
        <span><a href="https://celttechie.github.io/">celttechie.github.io</a></span>
        <span><a href="https://www.linkedin.com/in/bjarrett">linkedin.com/in/bjarrett</a></span>
        <span>U.S. Citizen (Clearance Eligible)</span>
    </div>
</div>

## Professional Summary

Systems Engineering Technical Leader and DevOps Engineer with 15+ years of enterprise platform leadership in bare-metal compute, Linux systems administration, enterprise virtualization, and Site Reliability Engineering (SRE)—including 7+ years of technical leadership at Cisco in the Webex FedRAMP environment on Cisco UCS, VMware, and OpenStack platforms. A methodical problem-solver who approaches infrastructure from first principles, favoring deterministic, declarative automation to eliminate repetitive operational toil, ensuring secure, high-uptime platform operations across 6,000+ production systems.

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

### **Cisco Systems** | Cloud Engineering Technical Leader
*Aug 2019 – July 2026 | Remote (USA)*

* **Federal ATO Governance & Emergency Zero-Day Response (Log4j / 6,000+ Systems):** Played an integral technical leadership role during the enterprise Log4j crisis across 6,000+ operational bare-metal and cloud systems under federal FedRAMP ATO governance. Authored custom Ansible inspection playbooks and Python tooling to rapidly assess the fleet and detect nested Java dependencies missed by commercial scanners; partnered directly with engineering teams to guide remediation, re-assessed systems to validate fixes, and compiled technical evidence defending the platform's ATO under strict federal deadlines.
* **Vulnerability Data Platform & Fleet UI Architecture (FastAPI, PostgreSQL, Tableau):** Designed and maintained an internal FastAPI + PostgreSQL vulnerability portal (fed by automated Jira ETL) used by multiple engineering teams to triage issues and by leadership to track fleet status across the FedRAMP footprint. Resolved operational alert fatigue caused by fragmented 1:1 server-to-ticket reporting by condensing issues into actionable fleet views; extended platform with Tableau dashboards tracking SLA severity.
* **Cross-Discipline Technical Translation & Federal Deviation Authority:** Served as the technical bridge between software developers, storage engineers, and networking teams, demystifying abstract CVEs, kernel vulnerabilities, and DISA STIG benchmarks into actionable code and configuration remediation paths. Authored formal technical compliance deviation and risk justification packages submitted to the federal PMO for acceptable operational risks.
* **DevSecOps & Compliance Automation (STIG XCCDF/XML & Qualys API):** Engineered custom Python automation querying the Qualys API to ingest raw compliance assessment results and correlate them with parsed DISA STIG XCCDF (XML) benchmark data, mapping running Linux server configurations directly to federal controls. Streamlined data handoffs for checklist generation, eliminating hundreds of engineering hours of manual compliance data correlation.
* **Engineering Mentorship & Technical Guidance:** Mentored junior and mid-level engineers on Linux diagnostics, root-cause troubleshooting, and operational practices. Supported hiring through technical interviewing and structured onboarding across distributed remote teams.

### **Cisco Systems** | Cloud Systems Engineer & Lead Compute Engineer
*Jan 2017 – Aug 2019 | Remote (USA)*

* **Lead Compute Engineering & Virtualization Operations:** Managed enterprise virtualization clusters on VMware vSphere and Cisco UCS bare metal across commercial and FedRAMP data centers. Served as lead compute engineer resolving virtualization performance bottlenecks, maintaining strict federal uptime SLAs, and supporting Cisco MDS Fibre Channel SAN switch fabrics and zoning.
* **Enterprise Identity Architecture & SOC Collaboration (FreeIPA/HBAC):** Architected and deployed an automated, high-availability FreeIPA cluster in OpenStack using Ansible to replace a legacy 389 Directory Server environment. Partnered with the Security Operations Center (SOC) to establish fine-grained Host-Based Access Control (HBAC) rule sets, guiding application teams on service permissions and standardizing zero-trust access control across 2,000+ hosts.
* **Compute Security & Bastion Infrastructure:** Hardened VMware vSphere clusters, Cisco UCS bare metal, and FedRAMP bastion environments. Architected and maintained secure remote access infrastructure, managing hardened Linux bastion hosts, Active Directory domain controllers, and LDAP directory services across 2,000+ systems.

### **Select Group @ Cisco** | Cloud DevOps/QA Engineer (Contract)
*Feb 2016 – Jan 2017 | Remote (USA)*

* **Nova Scheduler Performance Optimization:** Identified and removed redundant Nova Scheduler filters in OpenStack for Cisco's InterCloud Services (OpenStack-on-OpenStack on Cisco UCS bare metal), reducing instance scheduling time for 700 nodes from 20 seconds to 5 seconds—a **75% improvement** in orchestration speed.
* **Bare-Metal PXE Provisioning & Automation at Scale:** Engineered automated bare-metal deployment and provisioning workflows using PXE boot and Ansible playbooks across hundreds of production servers within Cisco's InterCloud Services. Automated ongoing configuration management and system maintenance via lights-out management (LOM) interfaces.
* **Infrastructure Evaluation & Stability Engineering:** Stood up RHUI (Red Hat Update Infrastructure) and Proxmox clusters for Proof-of-Concept (PoC) assessments. Diagnosed and resolved a critical race condition involving `cloudbase-init` on Windows images within OpenStack, eliminating intermittent reboots during instance setup.
* **Cloud QA & Orchestration Testing:** Managed global test cycles for Compute and Heat components during major cloud upgrades; developed Python, Bash, and Ansible scripts to perform comprehensive automated orchestration tests.

### **Australian Laboratory Services** | Senior Systems & Storage Administrator
*Sep 2014 – Jan 2016 | Grand Junction, CO*

* **Distributed Storage Engineering (Ceph RBD & VMware ESXi):** Engineered an Ubuntu-based Ceph cluster for VMware ESXi hosts, benchmarking iSCSI vs. RBD performance to optimize block storage access. Leveraged Ceph RBD snapshots to manage automated database schema testing, enabling a major production database upgrade with zero errors.
* **Infrastructure Automation & Data Integrity:** Implemented SaltStack to manage Linux virtual environments and automate rapid provisioning of Ceph storage nodes and virtual machine resources. Wrote custom Python (SQLAlchemy) verification scripts to audit SQL foreign keys during data migration.
* **System Telemetry & Network Reliability:** Integrated proactive telemetry checks into Nagios and Observium to monitor production systems, decreasing service restarts from weekly to quarterly. Diagnosed WAN/VPN bottlenecks and upgraded gateway hardware to double network throughput.

### **Foundational Systems, Infrastructure & Testing Experience**
*Prior Systems Foundations (StorageSoft / Phoenix Technologies)*

* **Enterprise Lab Architecture & Infrastructure Overhaul:** Following a corporate split, redesigned, rebuilt, and managed the company's internal network, server infrastructure, and heterogeneous multi-OS test laboratories across diverse storage controllers and network topologies.
* **Quality Engineering & Automated Test Workflows:** Promoted from contractor to QA Lead and Manager of Testing & Technical Support. Established the organization's first formal bug-tracking system and standardized testing workflows; structured automated validation suites across Windows and Linux environments, bridging software defects directly to core engineering teams.

## Systems Leadership & Robotics Mentorship

### **FIRST Robotics Team 3160 (F.R.O.G.)** | Lead Engineering & Systems Mentor
*2014 – Present (10+ Years)*

* **Real-Time Control Systems & Telemetry:** Mentored high school engineering students and developed Python (RobotPy) software for real-time robot control loops, swerve drive kinematics, distributed CAN bus telemetry, sensor fusion, and AprilTags computer vision.
* **Subsystem Testing & Physics Simulation:** Built automated testing routines and physics simulations to validate robot mechanisms and drive code prior to hardware deployment; diagnosed critical mechanical, electrical, and sensor failures under intense tournament constraints.

## Military Service, Clearance & Education

* **Airborne Warning and Control Radar Journeyman (AWACS)** | **United States Air Force**  
  *Maintained and repaired high-power microwave radar transmitters, high-voltage power supplies, and analog/digital signal processing electronics under stringent operational defense standards. Honorable Discharge.*
* **Security Clearance Status:** U.S. Citizen eligible for immediate Secret / Top Secret security clearance sponsorship; extensive career background operating within FedRAMP Moderate (HHS PMO ATO) and DISA STIG compliance boundaries.
* **Education & Continuous Learning:** Engineering Coursework, Colorado School of Mines. Ongoing technical specialization in Kubernetes/OpenShift container platforms, accelerated AI infrastructure, Infrastructure as Code (OpenTofu, Ansible), and Federal Zero-Trust Architectures.
