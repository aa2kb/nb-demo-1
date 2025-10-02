# Test dataset for Ragas evaluation with reference answers

dataset = {
    "question": [
        # Abu Dhabi Procurement Standards
        "What is the objective of the Abu Dhabi Procurement Standards?",
        "Who issues the Abu Dhabi Procurement Standards?",
        "What is the principle behind transparency in procurement?",
        "What must a purchase order include according to the standards?",
        "How do Delivery Terms and Payment Terms relate to a Purchase Order?",

        # Information Security (NESA IA Standards)
        "What is the purpose of the UAE Information Assurance Standards?",
        "Which authority developed the UAE IA Standards?",
        "What is meant by a risk-based approach in UAE IA Standards?",
        "What are the main phases of the Information Assurance lifecycle?",
        "Who are the key stakeholders in implementing the UAE IA Standards?",

        # Procurement Manual (Ariba Aligned)
        "What is the purpose of the Procurement Manual (SAP Ariba Aligned)?",
        "Which procurement activities are exempted from the Procurement Manual?",
        "What is the role of the Government Procurement Office (GPO)?",
        "How are Common Categories classified?",
        "What are the three types of Procurement Benefits?",

        # Procurement Manual (Business Process)
        "What is the scope of the Procurement Manual (Business Processes)?",
        "What are Entity-Specific Categories?",
        "What taxonomy is recommended for category classification?",
        "What does the Requisition to Pay (R2P) process cover?",
        "What is the role of Supplier Master Data Management?"
    ],
    "contexts": [
        # Abu Dhabi Procurement Standards
        ["The Abu Dhabi Procurement Standards aim to establish clear rules for procurement across government entities ensuring fairness, transparency, and efficiency."],
        ["The Abu Dhabi Executive Council issues the Procurement Standards."],
        ["The principle of transparency ensures that all procurement processes are open, with clear communication and equal opportunity for suppliers."],
        ["Purchase Orders must clearly include Delivery Terms and Payment Terms as part of the contract agreement."],
        ["Delivery Terms (C4) and Payment Terms (C5) are mandatory elements agreed upon during Purchase Order creation under Abu Dhabi Procurement Standards."],

        # Information Security (NESA IA Standards)
        ["The purpose of the UAE IA Standards is to raise the minimum protection level of information assets and systems across implementing entities in the UAE."],
        ["The National Electronic Security Authority (NESA) developed the UAE IA Standards."],
        ["A risk-based approach ensures entities identify and treat the most critical vulnerabilities based on their potential impact."],
        ["The Information Assurance lifecycle includes: understanding requirements, conducting risk assessments, implementing controls, monitoring performance, and continual improvement."],
        ["Key stakeholders include NESA, sector regulators, and individual entities, each responsible for implementing, reporting, and monitoring compliance with IA Standards."],

        # Procurement Manual (Ariba Aligned)
        ["The Procurement Manual (SAP Ariba Aligned) provides operational procedures, reinforcing Procurement Standards, the Procurement Charter, and the Delegation of Authority."],
        ["Exemptions include staff salaries, direct employment contracts, general admin expenses, inter-government agreements, sponsorships, artworks, copyright fees, travel reimbursements, and mandatory fees."],
        ["The GPO consolidates demand, manages sourcing for Common Categories, provides shared services, maintains the procurement framework, and manages the eGate platform."],
        ["A category procured by five or more entities may be considered a Common Category, typically managed by the GPO."],
        ["Procurement Benefits are classified into Cost Reduction, Cost Avoidance, and Cash Impact."],

        # Procurement Manual (Business Process)
        ["The Procurement Manual applies to all procurement activities by government entities and the GPO, unless exempted by the Executive Council."],
        ["Entity-Specific Categories are those categories unique to a specific government entity and managed by that entity’s procurement team."],
        ["The recommended taxonomy for classification is the UNSPSC (United Nations Standard Products and Services Code)."],
        ["The Requisition to Pay process includes creating purchase requisitions, purchase orders, receiving goods/services, and invoice reconciliation."],
        ["Supplier Master Data Management involves registering, qualifying, deactivating, and managing supplier data, fully handled by the GPO."]
    ],
    "reference_answers": [
        # Abu Dhabi Procurement Standards
        "The objective is to ensure fairness, transparency, and efficiency in government procurement.",
        "The Abu Dhabi Executive Council.",
        "Transparency means processes are open, with clear communication and equal supplier opportunity.",
        "It must include Delivery Terms and Payment Terms.",
        "They are mandatory contractual elements in a Purchase Order under the standards.",

        # Information Security (NESA IA Standards)
        "To raise the minimum level of protection for information assets and systems in the UAE.",
        "The National Electronic Security Authority (NESA).",
        "It ensures entities prioritize risks and apply controls based on critical vulnerabilities.",
        "Understanding requirements, risk assessment, implementing controls, monitoring, and continual improvement.",
        "NESA, sector regulators, and implementing entities are the key stakeholders.",

        # Procurement Manual (Ariba Aligned)
        "To provide operational procedures aligned with Procurement Standards, the Charter, and Delegation of Authority.",
        "Salaries, direct contracts, admin expenses, government agreements, sponsorships, artworks, copyrights, travel reimbursements, and mandatory fees.",
        "To consolidate demand, manage common categories, provide shared services, and operate the procurement framework and platform.",
        "If five or more entities procure a category, it becomes a Common Category managed by the GPO.",
        "Cost Reduction, Cost Avoidance, and Cash Impact.",

        # Procurement Manual (Business Process)
        "It applies to all government procurement activities unless excluded by the Executive Council.",
        "Categories specific to a single entity, managed by that entity’s procurement team.",
        "The UNSPSC taxonomy is recommended for classification.",
        "Covers requisitions, purchase orders, goods receipt, and invoice reconciliation.",
        "Registering, qualifying, and managing supplier data, executed by the GPO."
    ]
}
