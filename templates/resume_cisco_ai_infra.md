<div class="resume-header">
    <h1>Brian Jarrett</h1>
    <div class="subtitle">Systems Engineering Technical Leader | Solutions Architecture & SRE</div>
    <div class="contact-info">
        <span>Grove, OK</span>
        <span><a href="mailto:celttechie@gmail.com">celttechie@gmail.com</a></span>
        <span><a href="https://celttechie.github.io/">celttechie.github.io</a></span>
        <span><a href="https://www.linkedin.com/in/bjarrett">linkedin.com/in/bjarrett</a></span>
    </div>
</div>

## Professional Summary

Systems Engineering Technical Leader and Solutions Architect with a 30-year foundational background in bare-metal compute, Linux systems administration, enterprise virtualization, and Site Reliability Engineering (SRE)—including 7+ years of technical leadership at Cisco in the Webex FedRAMP environment on Cisco UCS/FIC, VMWare and OpenStack platforms. A methodical problem-solver who approaches infrastructure from first principles, favoring deterministic, consistent, and predictable automation to eliminate repetitive tasks, ensuring secure and stable platform operations across 6,000+ production systems.

Proactively expanding on this deep systems foundation through hands-on technical research and lab engineering: built dedicated testbeds exploring Single-Node OpenShift (SNO 4.16+), host PCIe VFIO GPU passthrough, the NVIDIA GPU Operator lifecycle, high-throughput vLLM model serving, and Day-2 SRE operational recovery runbooks. Combines proven enterprise compute operations with an active drive to understand, explore, and operationalize emerging accelerated AI infrastructure.

## Core Technical Competencies

<div class="skills-section">
    <div class="skills-column">
        <strong>Enterprise Systems & Compute:</strong>
        <ul>
            <li>Cisco UCS Bare-Metal & CIMC/LOM</li>
            <li>Linux Administration (RHEL, Ubuntu)</li>
            <li>Distributed Scheduling (OpenStack Nova)</li>
            <li>Virtualization (VMware ESXi, KVM, Proxmox)</li>
            <li>Ceph Block Storage (RBD) & iSCSI</li>
            <li>Storage Fabric Basics (Cisco MDS FC)</li>
        </ul>
    </div>
    <div class="skills-column">
        <strong>SRE, Automation & Governance:</strong>
        <ul>
            <li>SRE Practices & Root Cause Analysis</li>
            <li>Incident Leadership (Log4j / 6,000+ Nodes)</li>
            <li>Deterministic Automation (Ansible, OpenTofu)</li>
            <li>Python Tooling, Shell & REST APIs</li>
            <li>FreeIPA / Identity & HBAC Access Control</li>
            <li>FedRAMP Moderate & DoD STIGs (XCCDF)</li>
        </ul>
    </div>
    <div class="skills-column">
        <strong>Active Technical Research (Lab):</strong>
        <ul>
            <li>Red Hat OpenShift (SNO) & K8s Concepts</li>
            <li>PCIe VFIO GPU Passthrough & IOMMU</li>
            <li>NVIDIA GPU Operator & Time-Slicing</li>
            <li>vLLM Serving (Continuous Batching)</li>
            <li>SRE Runbooks (PCIe Resets, Post-Mortems)</li>
            <li>NVMe Storage Tuning for etcd (<10ms)</li>
        </ul>
    </div>
</div>

## Applied Technical Research & Lab Projects (Personal R&D)

### **OpenShift & Kubernetes AI Infrastructure (openshift-ai-infrastructure)**
**Hands-on Exploratory Research Testbed (2026)**

*   **Hardware & Driver Exploration:** Configured host PCIe VFIO driver binding and IOMMU group isolation on dedicated Xeon hardware to explore bare-metal CUDA execution inside containers.
*   **Operator Lifecycle:** Deployed NVIDIA GPU Operator with CRI-O Container Device Interface (CDI); evaluated time-slicing configuration to understand GPU sharing mechanisms.
*   **Model Serving Evaluation:** Deployed an OpenAI-compatible vLLM serving engine to test continuous batching and PagedAttention behavior under load; explored declarative KServe/RHOAI overlays.
*   **SRE Runbooks & Post-Mortems:** Authored operational runbooks for PCIe bus recovery and node evacuation, including documenting real hardware incident RCAs (diagnosing Linux kernel D-state mutex deadlocks and SNO single-GPU scheduling contention).

### **Single-Node OpenShift Platform Substrate (openshift-sno-lab)**
**Automated OpenShift SNO Deployment Testbed (2026)**

*   **Infrastructure Substrate:** Automated Single-Node OpenShift (SNO 4.16+) deployment via OpenTofu and KVM/libvirt, ensuring platform provisioning is strictly isolated from workload layers.
*   **Storage & Network Fundamentals:** Tuned NVMe storage pools (`cache=none`, `io=threads`) to satisfy etcd fsync latency (<10ms); built peer-bastion split-DNS and HAProxy ingress on isolated virtual networks.
*   **Declarative OS Configuration:** Explored RHCOS MachineConfigs for boot-time 1GB HugePages and kernel IOMMU arguments; enforced zero-trust SSH via native OpenTofu Ed25519 key generation.

## Professional Experience

### **Cisco Systems | Cloud Engineering Technical Leader**
**Aug 2019 – July 2026 (Remote)**

*   **Federal ATO Governance & Enterprise Log4j Response (HHS PMO):** Played a central technical role in the enterprise Log4j response across 6,000+ bare-metal and cloud systems under HHS PMO FedRAMP ATO governance. Built custom Ansible/Python inspection tooling locating nested libraries missed by commercial scanners, verified remediation, and compiled PMO evidence packages defending the ATO.
*   **Vulnerability Data Platform & Fleet UI Architecture (FastAPI, PostgreSQL, Tableau):** Designed and maintained an internal FastAPI + PostgreSQL vulnerability portal (fed by automated Jira ETL) used by engineering teams to triage issues and by leadership to track fleet status across the FedRAMP footprint; extended with Tableau dashboards tracking SLA severity.
*   **Cross-Discipline Technical Translation & Federal Deviation Authority:** Served as technical bridge across software, storage, and networking teams, translating complex CVEs and DISA STIGs into actionable remediation paths. Authored formal technical compliance deviation and risk justification packages submitted to the federal PMO.
*   **Engineering Mentorship & Technical Guidance:** Mentored junior and mid-level engineers on Linux diagnostics, root-cause troubleshooting, and operational practices. Supported hiring through technical interviewing and structured onboarding across distributed remote teams.

### **Cisco Systems | Cloud Systems Engineer & Lead Compute Engineer**
**Jan 2017 – Aug 2019 (Remote)**

*   **Lead Compute Engineering & Virtualization Operations:** Managed enterprise virtualization clusters on VMware vSphere and Cisco UCS bare metal, serving as lead compute engineer maintaining high availability, strict federal SLAs, and supporting Cisco MDS Fibre Channel SAN switch fabrics.
*   **Enterprise Identity Architecture & SOC Collaboration (FreeIPA/HBAC):** Architected and deployed an automated, high-availability FreeIPA cluster in OpenStack via Ansible to replace legacy 389 DS. Partnered with the SOC to establish fine-grained Host-Based Access Control (HBAC) policies, guiding application teams on service permissions and standardizing access control across 2,000+ hosts.

### **Select Group @ Cisco | Cloud DevOps/QA Engineer (Contract)**
**Feb 2016 – Jan 2017 (Remote)**

*   **Nova Scheduler Performance Optimization:** Identified and removed redundant Nova Scheduler filters in OpenStack for Cisco's InterCloud Services (OpenStack-on-OpenStack on Cisco UCS bare metal), reducing instance scheduling time for 700 nodes from 20s to 5s—a **75% improvement** in orchestration speed.
*   **Infrastructure Evaluation & Bare-Metal Automation:** Configured and evaluated RHUI (Red Hat Update Infrastructure) and Proxmox clusters for InterCloud PoC assessments. Automated bare-metal server configuration using Ansible via lights-out management (LOM) interfaces. Troubleshot and resolved a critical OpenStack `cloudbase-init` race condition.
*   **Cloud QA & Orchestration:** Managed global test cycles for Compute and Heat components during cloud upgrades; developed Python, Bash, and Ansible scripts for automated orchestration test suites.

### **Australian Laboratory Services | Senior Systems & Storage Administrator**
**Sep 2014 – Jan 2016 (Grand Junction, CO)**

*   **Distributed Storage & Automation:** Engineered an Ubuntu-based Ceph cluster for VMware ESXi hosts, benchmarking iSCSI vs. RBD performance. Used Ceph RBD snapshots for automated schema migration testing. Automated node provisioning via SaltStack; reduced service restarts with Nagios/Observium telemetry.

### **Garfield County School District 16 | Senior Systems/Network Administrator**
**Oct 2002 – Jun 2014 (Parachute, CO)**

*   **Infrastructure Modernization & Networking:** Modernized enterprise systems, deploying district-wide Cisco CallManager, thin-client computing, and high-speed Ruckus wireless bridges (+6,500% bandwidth). Built custom Python/Flask automation syncing databases with Active Directory.

### **Foundational Experience | Systems Engineering, Software QA & Avionics**
**1991 – 2002 (Various)**

*   **Solutions Engineer/Software QA Lead (StorageSoft/Phoenix Tech):** Software QA testing workflows for ImageCast disk cloning tools; designed test lab environments.  Managed tech support and testing departments. 
*   **Airborne Radar Journeyman (U.S. Air Force):** Repaired high-power microwave systems, high-voltage circuits, and digital/analog systems on AWACS aircraft.

## Education & Certifications
--8<-- "docs/sections/education.md"
