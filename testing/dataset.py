# Test dataset for Ragas evaluation with long-form reference answers

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
        "The primary objective of the Abu Dhabi Procurement Standards is to create a clear and standardized framework for procurement across all government entities in Abu Dhabi. These standards are designed to promote fairness, ensure full transparency, and improve efficiency in how public funds are spent, while also enabling accountability and consistent practices in line with the emirate’s governance model.",
        "The Abu Dhabi Procurement Standards are officially issued and overseen by the Abu Dhabi Executive Council. This body ensures that the rules and regulations are applied consistently across government entities and has the authority to approve updates, exemptions, or amendments where necessary.",
        "Transparency in procurement refers to the principle that all procurement activities must be conducted in an open and visible manner. This includes providing equal opportunity for suppliers, making procurement decisions based on clear and published criteria, and ensuring that information about processes and outcomes is shared in a way that fosters trust and reduces the potential for bias or corruption.",
        "According to the Abu Dhabi Procurement Standards, every purchase order must include both Delivery Terms and Payment Terms. These elements form a mandatory part of the contract agreement between a government entity and a supplier, ensuring that responsibilities for delivery timelines and payment obligations are clearly documented and agreed upon by both parties.",
        "Delivery Terms (C4) and Payment Terms (C5) are integral elements of a Purchase Order. They must be explicitly agreed upon during the creation of a Purchase Order, as they define when and how the supplier will deliver the goods or services, and under what conditions and timeline the government entity will process the payment. This ensures legal clarity and reduces future disputes.",

        # Information Security (NESA IA Standards)
        "The UAE Information Assurance Standards (IA Standards) were created to establish a national benchmark for cybersecurity across both public and private sector entities. Their purpose is to raise the baseline of protection for critical information assets and IT systems, ensuring that all organizations operating in the UAE adopt a consistent approach to risk management, system hardening, and secure operations.",
        "The UAE IA Standards were developed by the National Electronic Security Authority (NESA), which is the federal authority responsible for establishing and enforcing cybersecurity frameworks within the country. NESA designed the standards in consultation with sector regulators and government entities to ensure consistency across industries.",
        "The risk-based approach within the IA Standards requires entities to focus their security efforts on the areas of greatest potential impact. Instead of applying uniform controls across the board, organizations are encouraged to perform risk assessments, identify critical vulnerabilities, and allocate resources to mitigate the most severe threats first, thereby maximizing the effectiveness of their security programs.",
        "The Information Assurance lifecycle described in the IA Standards consists of several phases: understanding the legal and regulatory requirements, conducting a risk assessment, implementing the necessary technical and organizational controls, continuously monitoring performance, and engaging in ongoing improvement. Together, these phases create a sustainable cycle of security governance.",
        "The key stakeholders in implementing the UAE IA Standards include NESA, which defines the standards; sector regulators, who enforce them in their respective domains; and individual government and private entities, who must implement, monitor, and report on compliance. Collectively, they ensure a nationwide consistent application of information assurance practices.",

        # Procurement Manual (Ariba Aligned)
        "The purpose of the Procurement Manual (SAP Ariba Aligned) is to serve as a comprehensive operational guide for procurement practitioners across Abu Dhabi government entities. It explains how the overarching Procurement Standards, Procurement Charter, and Delegation of Authority (PDoA) are practically applied within daily processes. It also provides step-by-step procedures supported by the SAP Ariba platform, ensuring consistency, compliance, and efficiency.",
        "The Procurement Manual includes a set of exemptions that clearly outline which activities do not fall under its scope. These exemptions cover areas such as salaries and staff benefits, direct employment contracts that cannot be tendered, general administrative expenses like utilities and subscriptions, government-to-government agreements, sponsorships and grants, the purchase of artworks and artifacts, copyrights and licenses, ad-hoc travel reimbursements, and mandatory fees like court duties and taxes.",
        "The Government Procurement Office (GPO) plays a central role by acting on behalf of multiple entities to consolidate demand, negotiate better terms with suppliers, and manage sourcing for Common Categories. It also provides shared services such as supplier registration, training, and master data management, maintains the overall procurement framework, and manages the government’s eGate procurement platform.",
        "Common Categories are those goods or services that are procured by five or more government entities. Once classified as a Common Category, responsibility for managing sourcing and supplier performance shifts to the Government Procurement Office, ensuring economies of scale and consistency in contract management.",
        "Procurement Benefits are categorized into three types: Cost Reduction, which refers to direct reductions in the baseline cost; Cost Avoidance, which refers to preventing future cost increases through measures like efficiency improvements; and Cash Impact, which accounts for one-time financial changes such as improved payment terms or asset sales.",

        # Procurement Manual (Business Process)
        "The Procurement Manual (Business Processes) applies to all procurement activities carried out by Abu Dhabi government entities and the Government Procurement Office. Its scope is comprehensive, covering every stage of the procurement lifecycle, from strategy and sourcing to contract management and supplier performance, unless a specific exemption is granted by the Abu Dhabi Executive Council.",
        "Entity-Specific Categories are categories of goods or services that are unique to the needs of a single government entity. Unlike Common Categories, which are consolidated and managed by the GPO, these categories remain under the direct responsibility of the individual entity’s procurement team.",
        "For category classification, the Procurement Manual recommends the adoption of the United Nations Standard Products and Services Code (UNSPSC). This taxonomy provides a structured four-level classification system—Segment, Family, Class, and Commodity—that enables standardization, demand consolidation, supplier segmentation, and risk profiling.",
        "The Requisition to Pay (R2P) process covers the entire transactional workflow of procurement. It starts with the creation of a purchase requisition, proceeds to issuing a purchase order, continues with the receipt of goods or services, and ends with the reconciliation and payment of supplier invoices. This ensures traceability and accountability throughout the procurement process.",
        "Supplier Master Data Management is a critical function handled by the Government Procurement Office. It involves registering new suppliers, qualifying or disqualifying them, managing their activation or deactivation in the system, and ensuring that supplier information remains accurate, up-to-date, and compliant with procurement standards."
    ]
}
