
--- Page 1 ---

# NESA UAE INFORMATION ASSURANCE STANDARDS 

![img-0.jpeg](img-0.jpeg)

--- Page 2 ---

![img-1.jpeg](img-1.jpeg)

Digitized by Google

--- Page 3 ---

# 0 <br> ![img-2.jpeg](img-2.jpeg)

--- Page 4 ---

1 INTRODUCTION ..... 5
1.1 Background ..... 5
1.2 Purpose of the UAE IA Standards ..... 6
1.3 Layout of the UAE IA Standards ..... 7
2 UAE IA STANDARDS OVERVIEW ..... 9
2.1 Scope ..... 9
2.2 Related NESA Documents ..... 9
2.3 Entity, Sector, and National Contexts ..... 10
2.4 Information Assurance Lifecycle ..... 11
3 UAE IA STANDARDS IMPLEMENTATION ..... 12
3.1 Overview ..... 12
3.2 Risk-Based Approach ..... 12
3.3 Applicability of Controls ..... 15
3.4 Prioritization of Controls ..... 16
3.5 Key Stakeholders Roles and Responsibilities ..... 17
3.6 Key Success Factors ..... 19
4 COMPLIANCE WITH THE UAE IA STANDARDS ..... 21
5 SECURITY CONTROLS ..... 23
5.1 Control Structure ..... 23
5.2 Description of families of controls ..... 24
5.3 Management Controls ..... 26
M1 Strategy and Planning ..... 26
M2 Information Security Risk Management ..... 40
M3 Awareness and Training ..... 52
M4 Human Resources Security ..... 58
M5 Compliance ..... 64
M6 Performance Evaluation and Improvement ..... 74
5.4 Technical Controls ..... 79
T1 Asset Management ..... 79
T2 Physical and Environmental Security ..... 88
T3 Operations Management ..... 99
T4 Communications ..... 113
T5 Access Control ..... 127
T6 Third-Party Security ..... 145
T7 Information Systems Acquisition, Development and Maintenance ..... 150
T8 Information Security Incident Management ..... 170
T9 Information Systems Continuity Management ..... 180
ANNEX
Annex A Summary of Always Applicable Controls ..... 186
Annex B Summary of the Prioritized Controls ..... 189
Annex C Mapping of Controls against Leading Standards ..... 195
Annex D Mapping of Threats to Controls ..... 215
Annex E Sector and National Level Controls ..... 219
Annex F Terms and Definitions ..... 221
Annex G Bibliography ..... 226
APPENDICES
Appendices Sector-Specific Standards ..... 227

--- Page 5 ---

|  |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |   |  

--- Page 6 ---

# FOREWORD 

The increased adoption of Information Technology (IT), electronic communications, and cyberspace - comprising a global network of interdependent information technology infrastructures, telecommunications networks, and computer processing systems - has provided organizations in the UAE with a platform for delivering innovative services and stimulating economic development, as well as facilitating collaboration and communications among individuals. Our dependence on these technologies will continue to grow in the future, and therefore, the UAE Government is committed to the development of a secure national information and communications infrastructure for UAE organizations and individuals to realize the full potential of its benefits, in the face of an evolving set of related cyber threats.

As cyber threats such as hacktivism and cybercrime evolve, so must our efforts to defend against them in a coordinated and systematic manner. To align and direct national cybersecurity efforts, the UAE Government created the National Electronic Security Authority (NESA) to improve our national cybersecurity, and protect our national information and communications infrastructure. As part of this mandate, NESA developed the UAE Information Assurance (IA) Standards to provide requirements for raising the minimum level of IA across all relevant entities in the UAE.

The adoption of these Standards by UAE entities will sustain the benefits of a trusted digital environment for businesses and individuals across the nation. As cybersecurity is the shared responsibility of every organization and individual, collaboration and partnerships between the Government and private sector organizations are key to success. I am confident that our combined efforts will make great strides in achieving the UAE's national cybersecurity objectives and allow our nation's interests to thrive.

## JASSEM BU ATABA AL ZAABI

DIRECTOR GENERAL
NATIONAL ELECTRONIC SECURITY AUTHORITY

--- Page 7 ---

.

--- Page 8 ---

# (1) 

## HAPTER 01 INTRODUCTION

--- Page 9 ---

(1)
![img-3.jpeg](img-3.jpeg)

--- Page 10 ---

# 1.1 <br> BACKGROUND 

The adoption of Information Technology (IT) and electronic communication have greatly improved the efficiency and productivity of businesses and governments within the UAE, and facilitated collaboration of individuals within the nation and across the globe. Undoubtedly, IT and electronic communication have and will continue to play a pivotal role in the economic development of the UAE and the daily life of its citizens. Therefore, the UAE stands committed to the further development of its national IT and electronic communication infrastructure, as well as its cyberspace, to support economic development and provide an environment where the interests of its governments, businesses, and citizens can thrive.

The benefits of this technology adoption, however, come with a rapidly evolving set of cyber threats. These threats stem from a wide range of sources - including hacktivists, issue-motivated groups, and organized cybercrime syndicates - and represent national security concerns that can potentially disrupt critical national services and compromise critical information assets.

Mitigating cyber threats, and ensuring the development of a secure national information and communications infrastructure, and cyberspace, is a strategic priority for the UAE. To this end, NESA developed the UAE IA Standards as a critical element of the National Information Assurance Framework (NIAF) to provide requirements for elevating the level of IA across all implementing entities in the UAE.

--- Page 11 ---

The development of the UAE IA Standards is based on regional and global best practices including:

- ISO/IEC 27001:2005 "Information technology - Security techniques - Information security management systems - Requirements",
- ISO/IEC 27002:2005 "Information technology - Security techniques - Code of practice for Information security management",
- ISO/IEC 27005:2005 "Information technology - Security techniques -Information security risk management"
- ISO/IEC 27010:2012 "Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications"
- ISO/IEC 27032:2012 "Information technology - Security techniques - Guidelines for cybersecurity"
- NIST 800-53 Revision 4 "Security and Privacy Controls for Federal Information Systems and Organizations"
- Abu Dhabi Information Security Standards Version 1 and Version 2, developed by Abu Dhabi Systems and Information Centre (ADSIC)
- SANS 20 Critical Security Controls for Effective Cyber Defense Version 4.1

Moreover the development was guided by key principles including:

- Applicability of the common IA requirements across industries, and applicability of the sector-specific IA requirements across entities within each CIIP sector
- Support for the development of the entity, sector, and national-level views of cyber security, to address potential IA risks that emerge from the interconnectivity of entities and sectors
- Support the performance management and the evolution of the controls in these standards based on measuring and sharing effective performance indicators, as well as contributions from key stakeholders to support the ongoing development and refinement of these Standards

Compliance with these Standards will raise the level of national IA and help the UAE progress towards a more resilient national information and communication infrastructure, and cyberspace. All UAE government entities and other entities identified as critical ${ }^{1}$ by NESA are obligated to implement these Standards. However, NESA highly recommends all entities in the UAE to adopt these Standards on a voluntary basis, as applicable, in order to participate in raising the nation minimum-security levels.

[^0]
[^0]:    ${ }^{1}$ The process for NESA to designate an entity as "critical" is outlined in the UAE Critical Information Infrastructure Protection (CIIP) Policy produced by NESA.

--- Page 12 ---

# 1.2 

### 1.2 PURPOSE OF THE UAE IA STANDARDS

The purpose of the UAE IA Standards is to provide requirements to raise the minimum level of protection of information assets and supporting systems across all implementing entities in the UAE, as outlined in Section 2.1.

In particular, the UAE IA Standards provides:

- Description of how information assurance is achieved at the national, sector, and entity levels
- Enable a risk-based approach for the implementation of these Standards
- Outline of the roles and responsibilities of key stakeholders for the planning, development, implementation, and ongoing monitoring and improvement of these Standards
- Reference catalog of common information security controls to defend against common threats that exploit known cyber security vulnerabilities
- Realization for sectorial requirements through the provision of specialized controls to address sector-specific information assurance requirements
- Phased implementation approach to address the most common threats, facilitate the incremental adoption of these Standards, and optimize the value realized through implementation
- Definition of compliance from the perspective of these Standards and describe the approach that will be adopted by NESA to assess compliance
- Enabler for inter-entity and cross-sector communication to support information sharing and build national situational awareness

In summary, the implementation of these Standards will serve to improve the IA protection level of the UAE critical information infrastructure. As such, this document serves as the national UAE IA Standards that implementing entities have to demonstrate compliance with.

--- Page 13 ---

# 1.3 

## LAYOUT OF THE UAE IA STANDARDS

This section provides an overview of the layout of the UAE IA Standards to guide the readability of this document.

Overall, the UAE IA Standards is composed of seven chapters:

## CHAPTER 1: INTRODUCTION

This chapter outlines NESA's rationale for developing the UAE IA Standards and provides an overview of the document layout.

## CHAPTER 2: UAE IA STANDARDS OVERVIEW

This chapter outlines the scope of the document and describes the relationship of the UAE IA Standards with other national cyber security program documents published by NESA (e.g. UAE CIIP Policy). This chapter also describes how information assurance requirements are addressed at the national, sector, and entity levels following a lifecycle approach to progress the adoption and evolution of information assurance in the UAE.

## CHAPTER 3: UAE IA STANDARDS IMPLEMENTATION

This chapter outlines the implementation guidance for entities applying the UAE IA Standards. To help guide the implementation of these Standards, this chapter also provides an overview of the risk-based approach for the identification of applicable controls to be implemented in order to address risks in a manner commensurate with their potential impact. Moreover, this chapter outlines the roles and responsibilities of key stakeholders to provide clarity on how to plan, develop, implement, monitor, improve, and report on the implementation of these Standards. Lastly, this chapter concludes by outlining critical success factors for the effective implementation of these Standards.

--- Page 14 ---

# CHAPTER 4: COMPLIANCE WITH THE UAE IA STANDARDS 

This chapter provides a definition of compliance with respect to the requirements of these Standards, and outlines the approach that NESA will follow when evaluating compliance.

## CHAPTER 5: SECURITY CONTROLS

This chapter details the management and technical security controls, and describes the prioritization approach for implementing these controls, to guide the gradual and phased implementation of these Standards.

## CHAPTER 6: ANNEXES

This chapter provides key reference tools to help stakeholders understand and utilize the security controls including: grouping of controls by priority, cross-referencing of controls to equivalent controls in other key IA standards, mapping of controls against common threats they help to manage, and listing the controls that contain sector and national level requirements. Lastly, this chapter enhances the clarity of the document by providing terms and definitions and a bibliography.

## CHAPTER 7: APPENDICES

The appendices are designed to augment the common information assurance requirements (applicable to all sectors) with sector-specific requirements for all critical sectors as outlined in the UAE CIIP Policy.

--- Page 15 ---

# 1.1.2.2.2.2.2.3.2.3.3.3.4. 

## 1.1.2.2.3.1.2.3.2.4.1.2.5.2.6.2.7.8.9.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.88.89.90.91.92.93.94.95.96.97.98.99.10.11.12.13.14.15.16.17.18.19.20.21.22.23.24.25.26.27.28.29.30.31.32.33.34.35.36.37.38.39.40.41.42.43.44.45.46.47.48.49.50.51.52.53.54.55.56.57.58.59.60.61.62.63.64.65.66.67.68.69.70.71.72.73.74.75.76.77.78.79.80.81.82.83.84.85.86.87.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8.8

--- Page 16 ---

# HAPTERO2

## UAE IA STANDARDS OVERVIEW

![img-4.jpeg](img-4.jpeg)

--- Page 17 ---

# 0 

![img-5.jpeg](img-5.jpeg)

--- Page 18 ---

# 2.1 SCOPE 

The UAE IA Standards provides management and technical information security controls (henceforth referred to as "security controls") for entities to establish, implement, maintain, and continuously improve information assurance.

NESA will designate the critical entities, as per the UAE CIIP Policy, mandated to implement the UAE IA Standards and apply its requirements to the use, processing, storage, and transmission of information or data, and the systems and processes used for those purposes. This includes information in physical or electronic form that may be owned, leased, or otherwise in the possession, custody, or control of the entities.

--- Page 19 ---

# 2.2 

## RELATED NESA DOCUMENTS

The UAE IA Standards are critical element of the National Cyber Security Strategy (NCSS). Given this, these Standards rely on related and complementary policies issued under the NCSS. Table 1 below describes the relationships and dependencies between the UAE IA Standards and some other NCSS policies:

## TABLE 1: OVERVIEW OF DOCUMENTS RELATED TO THE UAE IA STANDARDS

| DOCUMENT | RELATION TO THE UAE IA STANDARDS |
| :-- | :-- |
| National <br> Information <br> Assurance <br> Framework <br> (NIAF) | The NIAF document outlines key building blocks of the <br> UAE information assurance capabilities and program, <br> and specifies the entity, sector, and national information <br> assurance interdependencies and requirements that need <br> to be addressed as part of the UAE IA Standards. |
| Critical <br> Information <br> Infrastructure <br> Protection (CIIP) <br> Policy | The CIIP Policy establishes the list of sectors and outlines <br> the process for the identification of critical entities where <br> the UAE IA Standards implementation is mandatory. |
| National <br> Cyber Risk <br> Management <br> Framework <br> (NCRMF) | The National Cyber Risk Management Framework details <br> the sector and national level risk management approach <br> with regards to Critical National Services and their Critical <br> Information Infrastructure, and provides guidelines on the <br> implementation of risk assessment in this regard. As such, <br> the UAE IA Standards outline key elements to be included <br> in an entity-level risk assessment, to support sector and <br> national risk assessment activities. |
| National Cyber <br> Information <br> Sharing Policy | The National Cyber Information Sharing policy outlines <br> key requirements for inter-entity and inter-sector <br> communication that serves as a key input to developing <br> national situational awareness. The UAE IA Standards <br> address these requirements by embedding respective <br> Information Sharing security controls that UAE entities will <br> implement. |

--- Page 20 ---

# 2.3 

## ENTITY, SECTOR, AND NATIONAL CONTEXTS

The entity, sector, and national contexts refer to the integrated relationships and interactions among individual sector entities, sector regulators, and NESA to form sector and national level views on prevailing IA requirements, corresponding adequacy of IA capabilities, and on-going situational awareness.

While IA Standards that exist today prescribe requirements for the entity level, they do not take into account the IA issues that emerge from the systemic interconnectivity of entities at the sector and national levels. This leads to two key shortcomings: first, continued exposure to security threats that no single entity is able to address individually (such as Advanced Persistent Threats), and second, an isolated approach to handling risks related to inter-sector dependencies, often leading to increased efforts, cost, and risk exposure of concerned sectors.

The UAE IA Standards includes minimum IA requirements and capabilities for UAE entities to integrate into the Sector and National Contexts (refer to Figure 2).

## FIGURE 2: NATIONAL, SECTOR AND ENTITY CONTEXT

![img-6.jpeg](img-6.jpeg)

--- Page 21 ---

The development of the sector and national contexts relies on the consolidation and analysis of key entity level information, in particular relating to the state of the UAE IA Standards implementation, risk assessment outcomes, as well as information relating to cyber security threats, risks and incidents. ${ }^{2}$ To enable the sector and national contexts, entities are required to submit UAE IA Standards implementation progress and key cyber security information to sector regulators, who consolidate and analyze the information to form a sector view of risks and assess the state of these Standards implementation. Similarly, sector regulators are required to submit the analyzed sector-level information to NESA, to form the national views on critical risks, situational awareness and state of these Standards implementation across sectors.

Having formed the national view of risks and state of these Standards implementation, NESA shares relevant risk and UAE IA Standards implementation best practices with the sector regulators to enhance the effectiveness of these Standards implementation, as well as the cyber incident management and the cyber risk management programs. Similarly, sector regulators share key risk and implementation related information with relevant entities to progress the implementation of these Standards, and enhance the effectiveness of the incident management and risk management programs.

In summary, the UAE IA Standards is designed to avoid the isolation created by a single-entity approach to IA, hence creating a stronger and more integrated approach for national information assurance.

[^0]
[^0]:    ${ }^{2}$ In the case of sectors with no regulator, NESA is responsible for consolidating and analyzing the information shared by entities, and developing the sector view of risks either directly or by identifying an entity to act as the "Information Assurance Sector Regulator"

--- Page 22 ---

# 2.4 

## INFORMATION ASSURANCE LIFECYCLE

The UAE IA Standards promotes a lifecycle approach for establishing, implementing, maintaining and continuously improving information assurance. This lifecycle approach ensures continual improvement of the UAE's information assurance capabilities based on well-defined activities:
A. UNDERSTANDING an entity's and / or sector's information security requirements and the need to establish a policy and objectives for information security
B. CONDUCTING risk assessments, identifying appropriate risk treatment actions, and selecting controls to manage the risks
C. IMPLEMENTING and operating security controls to manage information security risks in the context of the entity's or sector's overall business risks
D. MONITORING and reviewing the performance and effectiveness of the information security processes and controls
E. ENSURING continual improvement based on objective measurements

The continuous improvement aspect of the IA lifecycle ensures that IA capabilities are continuously adapted and evolved in line with changing requirements. The application of the IA lifecycle is facilitated best when integrated in the planning and governance activities of an entity or sector.

--- Page 23 ---

# 1.1.2.2.2.2.2.3.2.3.3.3.4. 

## 1.1.2.3.1.2.3.2.4.1.2.5.2.6.

--- Page 24 ---

# (1) 

## HAPTER 03

## UAE IA STANDARDS IMPLEMENTATION

--- Page 25 ---

(1)
![img-7.jpeg](img-7.jpeg)

--- Page 26 ---

# 3.1 OVERVIEW 

The purpose of this chapter is to explain key concepts related to the implementation of the UAE IA Standards such as the risk-based approach to information assurance and the applicability and prioritization of security controls. This chapter also highlights key stakeholder roles and responsibilities for the effective adoption and progression of the UAE IA Standards, and it lists critical implementation success factors.

The implementation of these Standards is meant to complement any existing information assurance programs at implementing entities. This Standard represents the sole point of reference for compliance against its requirements, as measured by the criteria associated with each of its security controls.

--- Page 27 ---

# 3.2 

## RISK-BASED APPROACH

In today's world, the cyber threat landscape is evolving rapidly at a pace where entities are challenged to keep up with the number and variety of threats. In the face of this growing threat landscape, entities need to adopt practical measures to defend their critical information and information infrastructure against their most critical vulnerabilities that could be exploited by threats. To this end, a risk-based approach provides entities with a pragmatic mean to identify their most critical vulnerabilities that could expose them to risks, and develop corresponding appropriate treatments.

Adopting a risk-based approach ensures that security controls are instituted in accordance with current risk assessments commensurate with the risk and magnitude of the impact that could result if critical information assets are compromised. The risk-based approach briefly outlined in these Standards summarizes a systematic methodology for identifying, estimating, evaluating, and treating identified entity-level risks. It consists of eight key activities as illustrated in Figure 3.

FIGURE 3: THE RISK-BASED APPROACH PROCESS
![img-8.jpeg](img-8.jpeg)

--- Page 28 ---

Performing a risk management is a key step towards the implementation of the UAE IA Standards as it helps entities identify, prioritize, and measure the effectiveness of the security controls that are needed to treat identified entity-specific risks. Critical entities implementing these Standards shall also refer to the National Cyber Risk Management Framework (NCRMF) which highlights the National Risk Management approach and process of Critical Information Infrastructure.

# ACTIVITY 1: ESTABLISHING THE ENVIRONMENT 

The risk assessment process should be initiated by establishing objectives, strategies, scope and parameters of the activities of the entity, or those parts of the entity where the risk management process is being applied. Further, criteria for assessing risks should be established in line with the entity's objectives, available resources, and the magnitude of impact that could result from the compromise of confidentiality, integrity and/or availability of information assets. Topics such as authenticity and non-repudiation could also be considered based on the entity context.

## ACTIVITY 2: RISK IDENTIFICATION

The entity should identify sources of risk, areas of impacts, events and their causes, and the potential consequences. The aim of this step is to generate a comprehensive list of risks based on the identified information security requirements. Because a risk that is not identified at this stage will not be included in further analysis, comprehensive identification is critical.

## ACTIVITY 3: RISK ESTIMATION

Risk estimation involves consideration of the causes and sources of risk in the form of threats and vulnerabilities, their impacts in terms of consequences of a loss of confidentiality, integrity and/or availability of information, and the likelihood that the potential impacts will occur. The risk should also take into account the effectiveness and efficiency of existing controls in addressing the current level of risk.

## ACTIVITY 4: RISK EVALUATION

Risk evaluation involves comparing the level of risk found during the risk estimation activity with risk criteria established at the beginning of the process as part of establishing the context (Activity 1). The objective is to determine which risks are outside acceptable parameters and therefore require treatment.

--- Page 29 ---

# ACTIVITY 5: RISK TREATMENT 

For each of the risks identified in the risk assessment, a number of treatment options can be considered and applied either individually, or in combination, for treating the risk. There are several options that are usually considered for treating risks; these options include:

- Risk Reduction - Reducing the risk by applying security controls. The selection of security controls should follow a risk-based approach by apply the first set of security controls that treat the highest risks identified during the Risk Evaluation (See 3.4 Prioritization of Controls).
- Risk Retention - Accepting the risk based on the entity's risk accepting criteria.
- Risk Avoidance - Avoiding the activity or condition causing the risk.
- Risk Transfer - Transferring the risk to another party.


## ACTIVITY 6: RISK ACCEPTANCE

The risk acceptance is the decision to accept residual risk by the management of the entity. The management based on the acceptance criteria should review and approve the treat plan and the residual risk.

## ACTIVITY 7: RISK MONITORING AND REVIEW

The results of the risk assessment and treatment process need to be monitored and reviewed for ongoing risk management, and to ensure their continued suitability. The monitoring and review of information security risks should be a planned part of the risk management process, and involve regular checking or surveillance as well as improvements when significant changes occur. The entity's monitoring and review processes should encompass all aspects of the risk management process, including the risk criteria, the identified assets, threats, risks, risk treatment options and security controls.

## ACTIVITY 8: RISK COMMUNICATION AND CONSULTATION

Communication and consultation with key stakeholders should take place during all stages of the risk management process. Therefore, plans for communication and consultation should be developed at an early stage. These should address issues relating to the risk itself, its causes, its consequences (if known), and the measures being taken to treat it. Effective external and internal communication and consultation should take place to ensure that stakeholders and those accountable for implementing the risk management process understand the basis on which decisions are made, as well as the reasons why particular actions are required.

--- Page 30 ---

# 3.3 

## APPLICABILITY OF CONTROLS

The concept of Applicability relates to the identification of security controls for treating entity-specific risks as outlined in [Step 5] of the risk assessment process described above (section 3.2).

The security controls included in these Standards are developed to treat a typical entity risk profile developed based on benchmark risk registers. While this common risk profile is widely applicable to implementing entities, NESA recognizes that entity risk profiles do differ based on their specific business and operational context. Given these differences, not all security controls provided in these Standards might be applicable to all entities. Therefore, these Standards require that the identification of the security controls be based on an entity risk assessment resulting in applicable security controls for the treatment of identified risks.

Prior to performing the risk assessment process, an entity should consider all security controls to be applicable. However, an individual entity may exclude some security controls on the basis of the risk assessment outcomes, provided that adequate justification is submitted to NESA.

Moreover, certain security controls included in these Standards represent requirements for instituting foundational IA capabilities within an entity, and as such, are considered "Always Applicable". Given their foundational role, the "Always Applicable" security controls shall be implemented by each relevant entity regardless of its risk assessment outcomes (refer to Annex 1 for a summary of "Always Applicable" controls).

In summary, the concept of Applicability identifies the security controls that are mandatory for implementation based on the list of applicable controls resulting from the entity risk assessment process, above and beyond the "Always Applicable" controls. In the absence of an entity risk assessment, all the security controls detailed in these Standards are deemed applicable and therefore mandatory for implementation.

--- Page 31 ---

# 3.4 

## PRIORITIZATION OF CONTROLS

The concept of Prioritization relates to grouping the UAE IA Standards security controls in order of importance for realizing a minimum level of information assurance protection, and for enabling a phased and incremental implementation of these Standards.

The prioritization approach of the UAE IA Standards is based on the relative impact of security controls in helping implementing entities to:

- Mitigate common threats
- Build foundational IA capabilities

Based on these criteria, the security controls are grouped into four priority levels - P1, P2, P3, and P4 in this order of importance - and the outcome of the prioritization is included in Annex 2.

While all the applicable security controls across the four priority levels are mandatory for critical entities implementing these Standards, they are required to begin implementing these Standards with P1 security controls given their highest relative impact in protecting against critical threats and building foundational information assurance capabilities.

Critical entities implementing these Standards may alter (promote or demote) the suggested priority of controls based on the outcomes of their risk assessment, with the exception of top priority controls (P1), which if applicable, may be augmented but never reduced (refer to Figure 4).

--- Page 32 ---

![img-9.jpeg](img-9.jpeg)

# FIGURE 4: CONCEPTUAL OVERVIEW OF PRIORITIZATION OF SECURITY CONTROLS

## UAE IA STANDARDS PRIORITIZATION

### PRIORITY 1 CONTROLS

### PRIORITY 2 CONTROLS

### PRIORITY 3 CONTROLS

### PRIORITY 4 CONTROLS

## ENTITY RISK ASSESSMENT

### PRIORITY 1 CONTROLS CAN BE AUGMENTED BUT NOT REDUCED

### PRIORITY 2 CONTROLS

### PRIORITY 3 CONTROLS

### PRIORITY 4 CONTROLS

## ENTITY RISK-BASED PRIORITIZATION

### PRIORITY 1 CONTROLS CAN BE AUGMENTED BUT NOT REDUCED

### PRIORITY 2 CONTROLS

### PRIORITY 3 CONTROLS

## PROMOTED TO HIGHER PRIORITY

### DEMOTED TO LOWER PRIORITY

--- Page 33 ---

# 3.5 

## KEY STAKEHOLDERS ROLES AND RESPONSIBILITIES

The successful implementation and progression of the UAE IA Standards is a shared responsibility among key stakeholders. Therefore, planning, development, implementation, as well as monitoring and reporting responsibilities are assigned to key stakeholders, as described in Table 2 below:

## TABLE 2: UAE IA STANDARDS STAKEHOLDER ROLES AND RESPONSIBILITIES

| \# | STAKEHOLDER | UAE IA STANDARDS ROLES AND RESPONSIBILITIES |
| :--: | :--: | :--: |
|  |  | ROLE |
|  |  | Provide strategic leadership and governance, coordinate stakeholder involvement for the development and implementation of the UAE IA Standards, and ensure ongoing compliance monitoring, and information sharing |
|  |  | RESPONSIBILITIES |
|  |  | IA STANDARDS PLANNING AND DEVELOPMENT |
|  |  | - Information Assurance Strategy Development - Provide strategic priorities for the development of the common and sector-specific requirements of the UAE IA Standards |
|  |  | - Security Requirements Development - Establish the UAE IA Standards security requirements in collaboration with key stakeholders including sector regulators, critical entities and cyber security experts |
|  |  | - UAE IA Standards Issuance - Approve and publish the UAE IA Standards as developed in collaboration with the key stakeholders |
| 1 | NESA | IA STANDARDS IMPLEMENTATION |
|  |  | NESA is responsible for facilitating the implementation of the UAE IA Standards, but does not have direct responsibilities in the implementation of these Standards within implementing entities |
|  |  | IA STANDARDS MONITORING AND REPORTING |
|  |  | - Compliance Monitoring - Review entity compliance self-assessment reports (as received from sector regulators), and recommend escalation for Compliance Audits or Testing where appropriate. |
|  |  | - Compliance Audit - Where appropriate, perform or commission compliance audits for validating entity self-assessment reports, and escalate further, if needed |
|  |  | - Compliance Testing - Where appropriate, perform or commission tests on relevant entities for ensuring that IA measures are in place, as well as their effectiveness |
|  |  | - Cyber Security Performance Reporting - Compile progress reports of the UAE IA Standards implementation across sectors and entities to steer the implementation efforts of these Standards |

--- Page 34 ---

| \# | STAKEHOLDER | UAE IA STANDARDS ROLES AND RESPONSIBILITIES |
| :--: | :--: | :--: |
| 2 | SECTOR <br> REGULATORS | ROLE <br> Actively contribute to the development of the UAE IA Standards in collaboration with NESA, developing sector specific IA requirements/ controls, and ensure UAE IA Standards compliance reporting as well as information sharing |
|  |  | RESPONSIBILITIES <br> IA STANDARDS PLANNING AND DEVELOPMENT <br> - UAE IA Standards Development - Provide input in the development of the UAE IA Standards security requirements in collaboration with NESA |
|  |  | - Sector-Specific Requirements Development - Augment UAE IA Standards with sector-specific requirements pertinent to each critical sector |
|  |  | IA STANDARDS IMPLEMENTATION <br> - Sector Regulators are responsible for facilitating the implementation of the UAE IA Standards, but do not have direct responsibilities in the implementation of these Standards within relevant entities |
|  |  | IA STANDARDS MONITORING AND REPORTING <br> - Sector Compliance Reporting - Consolidate critical entity compliance reports into a sector status update, and submit report to NESA to form a sector and potentially national view on the IA Standards implementation progress |
| 3 | IMPLEMENTING ENTITIES | ROLE <br> Implement the UAE IA Standards, and report on implementation progress and compliance, as well as share insights on security controls effectiveness |
|  |  | RESPONSIBILITIES <br> IA STANDARDS PLANNING AND DEVELOPMENT <br> - IA Standards Development - Provide input in the development the UAE IA Standards security requirements in collaboration with NESA through the IATFs ${ }^{3}$ <br> - Entity Implementation Plan Development - Develop an implementation plan for the adopting/applying the UAE IA Standards |
|  |  | IA STANDARDS IMPLEMENTATION <br> - Risk Assessment - Conduct risk assessment exercise to identify most critical vulnerabilities/threats and develop corresponding appropriate treatments <br> - IA Standards Implementation - Implement applicable controls from the UAE IA Standards |
|  |  | IA STANDARDS MONITORING AND REPORTING <br> - Compliance Reporting - Periodically update the relevant regulator (or NESA in the absence of a "Sector-Regulator") on the progress of UAE IA Standards implementation, and facilitate the audit and testing process whenever requested by the NESA |

[^0]
[^0]:    ${ }^{3}$ IATF (Information Assurance Technical Forum) is the forum that engage key stakeholders (such as industry leaders, experts, relevant entities, and sector regulators) to promote, discuss, and share relevant experiences with regards to the development and implementation of the UAE IA Standards

--- Page 35 ---

# 3.6 

## KEY SUCCESS FACTORS

The implementation of the UAE IA Standards and related security controls should be guided by the following key success factors:
A. PROVIDE appropriate awareness, training, and education within the entity, and communicate information assurance objectives to all managers, employees, and other organizational stakeholders (including partners, third-party vendors, etc.)
B. ESTABLISH a thorough understanding of the information assurance requirements, and in particular, the risk-based approach to identify applicable security controls and their respective implementation priorities
C. ADOPT a tailored approach and framework to establish, implement, maintain, and continuously improve information security in a manner that is consistent with the entity's culture
D. UNDERSTAND the means by which compliance with the UAE IA Standards will be measured and enforced

--- Page 36 ---

E. IMPLEMENT a measurement system to track compliance, evaluate performance in information assurance management, and provide feedback and suggestions for the improvement and refinement of the UAE IA Standards
F. ESCALATE critical cyber security information to sector regulators (or equivalents) to enable the development of sector and national level view of risks
G. PARTICIPATE, and contribute in sharing information assurance best practices and lessons learned with sector regulators and other implementing entities
H. ENSURE visible support and commitment from all levels of management
I. PROVISION adequate funding for all information assurance activities

--- Page 37 ---

|  1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  16 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  18 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  21 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  23 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  24 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  26 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  27 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  28 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  29 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  31 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  32 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  33 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  34 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  36 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  37 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  42 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  44 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  45 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  46 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  48 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  49 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  52 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  53 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  54 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  55 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  56 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  57 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  58 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  61 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  62 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  63 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  65 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  66 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  67 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  68 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  69 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  70 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  71 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  72 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  73 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  74 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  76 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  101 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  102 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  103 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  104 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  105 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  106 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  107 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  108 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  109 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  110 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  112 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  114 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  115 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  116 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  117 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  118 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  119 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  120 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  121 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  122 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  123 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  124 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  126 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  127 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  128 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  129 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  130 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  131 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  132 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  133 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  134 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  135 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  136 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  137 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  138 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  139 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  140 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  141 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  142 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  143 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  144 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  145 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  146 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  147 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  149 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  150 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  151 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  152 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  153 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  154 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  155 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  156 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  157 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  158 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  159 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  160 | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  161 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  162 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  163 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  164 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  165 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  166 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  167 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  168 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  169 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  170 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  171 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  172 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  173 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  174 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  175 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  176 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  177 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  177 | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

--- Page 38 ---

# (1) 

## HAPTER 04

COMPLIANCE WITH THE UAE IA STANDARDS

--- Page 39 ---

(3)
![img-10.jpeg](img-10.jpeg)

--- Page 40 ---

# 4.0 

## COMPLIANCE WITH THE UAE IA STANDARDS

The purpose of this chapter is to provide a definition of compliance with respect to the requirements of these Standards and to outline the measurement criteria and approach that NESA will follow when evaluating compliance.

Within the context of this Standard, compliance refers to the comparison between the requirements outlined in this Standard and the actual state of implementation of these requirements within an entity. This can be measured on an individual control basis, as well as the degree of compliance of an entity overall with the complete set of requirements. Increasing the level of compliance with the security controls provided in this Standard is the key to ensuring immediate and long lasting improvements of information assurance within the UAE and the overall success of the UAE's Information Assurance program.

--- Page 41 ---

To this end, NESA will ensure that an effective compliance monitoring scheme is in place which provides NESA with the visibility of the current status of compliance with this Standard and the activities needed for improving the overall security of the UAE's cyberspace. The compliance monitoring scheme is outlined in the UAE NIAF Governance and is based on the following four elements:

# CONTROLS 

All security controls specified in the UAE IA Standards need to be considered by each entity, and any entity wishing to claim compliance with these Standards shall implement these controls based on the following requirements:

- Controls that are "Always Applicable" - these security controls are essential and shall be implemented by any entity wishing to claim compliance with the UAE IA Standards. Omission of any of these controls is not acceptable and constitutes non-conformity.
- Controls that are applicable based on the risk assessment - the entity shall determine which of the security controls provided in the UAE IA Standards are applicable in its particular situation based on the results of the risk assessment. Any exclusion of these controls needs to be justified and evidence needs to be provided such that the associated risks have been accepted by accountable persons or authorizing entities.
The overall set of security controls that are "Always Applicable" and those security controls that have been determined as being applicable based on the risk assessment are "mandatory" for the entity to implement, and will be the basis of the compliance monitoring scheme.


## SUB-CONTROLS

For each of the security controls, a set of sub-controls are specified. These sub-controls specify mandatory implementation requirements. Also, it is expected that each entity claiming compliance shall implement the selected security controls by complying with the sub-controls during the implementation process as described below.

The entity shall implement all of the sub-controls of the "Always Applicable" security controls. Omission of any of these sub-controls is not acceptable and constitutes nonconformity to the UAE IA Standards.

The entity can decide to not implement a sub-control of a security control identified by the risk assessment, if this action is appropriately justified (e.g. following the risk assessment or due to decisions or circumstances in the entity), or to implement the sub-controls in a different way. Any deviation from the sub-controls needs to be justified and evidence needs to be provided such that the associated risks have been accepted by accountable persons or authorizing entities.

--- Page 42 ---

# PERFORMANCE INDICATORS 

Performance indicators are intended to provide entities implementing the UAE IA Standards with some basic guidelines to measure the quality and effectiveness of its compliance with the control sub-families and controls of this Standard. Entities implementing this Standard can deviate from these performance indicators, but are required to provide a reason for this deviation and to specify the new performance indicators when doing so.

For compliance with this Standard, entities need to use performance indicators to measure the quality and effectiveness of the implemented security controls.

## AUTOMATION, THREAT/VULNERABILITY DESCRIPTION FOR SUB-FAMILIES OF CONTROLS, AND IMPLEMENTATION GUIDANCE FOR CONTROLS

The information on possible automation and the implementation guidance for security controls are provided for information purposes only and can be implemented as the entity prefers, without any further explanation or justification. Descriptions of typical threats and vulnerabilities are also provided for information purposes.

In summary, NESA places a high level of importance on understanding and improving the level of compliance with this Standard as one of the core elements of increasing the level of success of the UAE's information assurance program. At the same time, NESA understands that individual entities face specific circumstances that require a certain level of flexibility to manage properly. As such, this Standard aims to strike an appropriate balance of mandatory requirements versus suggested security controls. This is based on the risk-based approach that each entity shall develop internally in order to make appropriate and justified decisions. Moreover, all implementing entities are welcomed and encouraged to share their experience in regard to the implementation of the security controls.

--- Page 43 ---

|  1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  16 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  18 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  21 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  23 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  24 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  26 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  27 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  28 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  29 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  31 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  32 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  33 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  34 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  36 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  37 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  42 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  44 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  45 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  46 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  48 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  49 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  52 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  53 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  54 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  55 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  56 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  57 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  58 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  61 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  62 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  63 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  65 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  66 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  67 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  68 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  69 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  70 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  71 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  72 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  73 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  74 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  76 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  101 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  102 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  103 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  104 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  105 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  106 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  107 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  108 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  109 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  110 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  112 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  114 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  115 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  116 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  117 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  118 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  119 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  120 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  121 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  122 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  123 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  124 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  126 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  127 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  128 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  129 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  130 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  131 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  132 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  133 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  134 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  135 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  136 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  137 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  138 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  139 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  140 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  141 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  142 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  143 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  144 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  145 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  146 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  147 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  149 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  150 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  151 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  152 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  153 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  154 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  155 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  156 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  157 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  158 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  159 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  160 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  161 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  162 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  163 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  164 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  165 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  166 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  167 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  168 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  169 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  170 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  171 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  172 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  173 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  174 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  175 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  176 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  177 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  178 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  179 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  180 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  181 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  182 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  183 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  184 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  185 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  186 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  187 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  188 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  189 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  190 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  191 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  191 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  1910 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  1911 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  1910 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

--- Page 44 ---

# HAPTER 05 SECURITY CONTROLS

--- Page 45 ---

(1)
![img-11.jpeg](img-11.jpeg)

--- Page 46 ---

# 5.1 

## CONTROL STRUCTURE

The hierarchy of control families, control sub-families and individual controls are structured as follows:

## CONTROL FAMILY STRUCTURE

| CONTROL <br> FAMILY NUMBER | CONTROL FAMILY NAME |
| :-- | :-- |
| OBJECTIVE | High level objective of the control family |
| PERFORMANCE <br> INDICATOR | Metrics that measure the effectiveness of the control family |

## SUB-FAMILY STRUCTURE

| CONTROL <br> SUB-FAMILY NAME | CONTROL SUB-FAMILY NUMBER |
| :-- | :-- |
| OBJECTIVE | High level objective of the control sub-family |
| PERFORMANCE <br> INDICATOR | Metrics that measure the effectiveness of the control sub-family |
| AUTOMATION <br> GUIDANCE | Description of procedures and / or tools to automate the <br> implementation of the control sub-family |
| RELEVANT THREATS <br> AND VULNERABILITIES | The most prevalent and damaging attack types against which the <br> control sub-family ensures protection |

--- Page 47 ---

# CONTROL STRUCTURE 

| CONTROL <br> NUMBER | CONTROL NAME | PRIORITY | P1 | P2 | P3 | P4 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | IDENTIFIES CONTROLS THAT ARE ALWAYS APPLICABLE AND CONTROLS THAT ARE APPLICABLE UNLESS OTHERWISE JUSTIFIED BY THE ENTITY'S RISK ASSESSMENT PROCESS |  |  |  |
| CONTROL | Control statement (e.g. The allocation and use of privileges should be restricted and controlled) |  |  |  |  |  |
| SUB-CONTROL | Sub-control statements that ensure optimal implementation of the control |  |  |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |  |  |
| Additional information on how to implement individual controls, and what it requires |  |  |  |  |  |  |
| Most of this information is derived from a variety of sources, including: <br> - ISO/IEC 27001:2005 "Information technology - Security techniques - Information security management systems - Requirements" <br> - ISO/IEC 27002:2005 "Information technology - Security techniques - Code of practice for Information security management" <br> - ISO/IEC 27005:2005 "Information technology - Security techniques -Information security risk management" <br> - ISO/IEC 27010:2012 "Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications" <br> - ISO/IEC 27032:2012 "Information technology - Security techniques - Guidelines for cybersecurity" <br> - NIST Special Publication 800-53 Revision 4 "Security and Privacy Controls for Federal Information Systems and Organizations" <br> - Abu Dhabi Information Security Standards Version 1 and Version 2, developed by Abu Dhabi Systems and Information Centre (ADSIC) <br> - SANS 20 Critical Security Controls for Effective Cyber Defense Version 4.1 |  |  |  |  |  |

--- Page 48 ---

# 5.2 

## DESCRIPTION OF FAMILIES OF CONTROLS

The security controls are structured under six management control families (addressing management requirements) described in Table 3 and nine technical control families (addressing technical requirements) described in Table 4.

## TABLE 3: DESCRIPTION OF MANAGEMENT CONTROL FAMILIES

| MANAGEMENT CONTROL FAMILIES | DESCRIPTION |
| :--: | :--: |
| STRATEGY AND PLANNING | An information security strategy shall be defined and operating model developed to adhere to the strategy. In addition, information security plans shall be developed for each major service to identify and mitigate the risks corresponding to each service |
| INFORMATION SECURITY RISK MANAGEMENT | An information security risk management process shall be implemented to conduct risk assessments, statements of applicability, security testing and evaluations of information security controls on applicable services |
| AWARENESS AND TRAINING | An awareness and training program shall be implemented to inform entities of risks associated with their activities and to ensure that entities are adequately trained to carry out their assigned information security responsibilities |
| HUMAN RESOURCES SECURITY | Human resources security requirements and security responsibilities shall be addressed prior employment, during employment, and after termination or change of employment |
| COMPLIANCE | Entities shall comply with legal requirements, security policies and technical standards |
| PERFORMANCE EVALUATION AND IMPROVEMENT | Entities shall ensure that information security performance is measured, analyzed and evaluated. |

--- Page 49 ---

# TABLE 4: DESCRIPTION OF TECHNICAL CONTROL FAMILIES 

| TECHNICAL CONTROL FAMILIES | DESCRIPTION |
| :--: | :--: |
| ASSET MANAGEMENT | Assets shall be managed and information shall be classified and labeled to ensure that assets including information receives an appropriate level of information security |
| PHYSICAL AND ENVIRONMENTAL SECURITY | Physical and environmental security measures shall be implemented to ensure critical or sensitive information systems are physically protected from unauthorized access, damage and interference and equipment is protected from physical and environmental threats |
| OPERATIONS MANAGEMENT | Operational procedures and responsibilities shall be developed, to ensure an adequate level of information security. In addition, backup, media handling, e-services security and monitoring shall be addressed to ensure protection against malicious code and spyware |
| COMMUNICATIONS | Network security and information sharing shall be addressed to ensure protection of information in transit |
| ACCESS CONTROL | Access control processes shall be developed to control access to information, to manage user access, control access to both internal and external network services, control access to operating systems, control access to applications and to apply appropriate protection when using mobile computing and teleworking services |
| THIRD PARTY SECURITY | Third party security shall be managed to ensure third parties implement and maintain the appropriate level of information security and service delivery, and information stored, processed, and retrieved, including via cloud services, is secure |
| INFORMATION <br> SYSTEMS <br> ACQUISITION, DEVELOPMENT AND MAINTENANCE | An information systems acquisition, development and maintenance process shall be implemented to prevent unauthorized modification or misuse of information in applications, to ensure that a cryptographic control policy is in place, to maintain security in development and support processes and to manage technical vulnerabilities |
| INFORMATION SECURITY INCIDENT MANAGEMENT | Information security events and weaknesses shall be reported and evidence of security incidents shall be collected and analyzed to ensure that information security events and weaknesses are properly communicated and security incidents adequately managed |
| INFORMATION SECURITY CONTINUITY MANAGEMENT | A business continuity management process shall be implemented to counteract interruptions to business activities and to protect critical business processes from failures of information systems |

--- Page 50 ---

# 5.3 

## MANAGEMENT CONTROLS

## M1 STRATEGY AND PLANNING

| M1 | STRATEGY AND PLANNING |
| :-- | :-- |
| OBJECTIVE | To provide an adequate organizational environment, leadership and <br> support for information security. |
| PERFORMANCE <br> INDICATOR | Percentage of incidents that are related to non-technical <br> information security problems over one month |


| M1.1 | ENTITY CONTEXT AND LEADERSHIP |
| :-- | :-- |
| OBJECTIVE | To establish leadership and a management framework to initiate <br> and control the implementation of information security within the <br> entity. |
| PERFORMANCE <br> INDICATOR | Measurement of the knowledge regarding information security <br> roles and responsibilities, role of top management, etc., e.g. by <br> using a test. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT THREATS <br> AND VULNERABILITIES | - Insufficient resources <br> - Non-compliance with information security controls <br> - Incompetent information security personnel <br> - Incomplete or not up to date documentation |

--- Page 51 ---

| M1.1.1 | UNDERSTANDING THE ENTITY AND ITS CONTEXT | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall determine external and internal factors that affect its ability to achieve the intended success of information security arrangements. |  |  |
| SUB-CONTROL | The entity shall determine: <br> 1) Interested parties that are relevant to its information security <br> 2) The requirements of these interested parties <br> 3) Factors related to its sector or national context <br> 4) Its internal capabilities <br> 5) Its organizational structure |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Before starting the design and implementation of information security within an entity, it is important to evaluate and understand both the external and internal context of this entity, since these can significantly influence the design of information security solutions. For the external factors, this activity should include topics such as: <br> A. The industry sector, legal, regulatory, financial, technological, economic, political, natural and competitive environment, whether international, national, regional or local <br> B. Key drivers and trends having impact on the information security objectives of the entity <br> C. Relationships with, and dependencies of, external stakeholders |  |  |  |
| The evaluation of internal factors should address topics such as: <br> A. Governance, organizational structure, roles and accountabilities <br> B. Capabilities, understood in terms of resources and knowledge (e.g. capital, time, people, processes, systems and technologies) <br> C. Information systems, information flows and decision making processes <br> D. Relationships with, and perceptions of, internal stakeholders <br> E. The form and extent of contractual relationships |  |  |  |

--- Page 52 ---

| M1.1.2 | LEADERSHIP AND <br> MANAGEMENT <br> COMMITMENT | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL
The entity's top management shall demonstrate leadership and commitment to information security.

SUB-CONTROL
Top management commitment shall:

1) Ensure the information security policy and the information security objectives are established and are compatible with the strategic direction of the entity
2) Ensure the integration of the information security requirements into the entity's processes
3) Ensure that the resources needed for information security are available
4) Communicate the importance of the effectiveness of information security management
5) Direct and support persons to contribute to the effectiveness of information security and conforming to the requirements of these Standards
6) Promote continual improvement
7) Support other relevant management roles to demonstrate their leadership as it applies to their areas of responsibility
8) Give direction to and participating in reviews of information security, including risks, controls and effectiveness, on a high level

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Top management commitment and its visible demonstration is one important contributor to the overall success of information security within an entity. This does not mean that top management is carrying out the actions listed above themselves, but they need to ensure that the actions do take place, and that they are concluded successfully.

One important part in these responsibilities is the assignment of appropriate resources, without which information security cannot succeed (see also M1.4.1 below). Another important aspect is the connection between business goals and requirements and information security. Ideally, this is a balance between these items, and it should never be the case that information security hinders the business. It should, of course, also not be the case that an entity takes any unjustified risks and neglects security. The final decision what takes preference has to be taken by top management.

Management should identify the needs for internal or external specialist information security advice, and review and coordinate results of the advice throughout the entity.

--- Page 53 ---

| M1.1.3 | ROLES AND RESPONSIBILITIES FOR INFORMATION SECURITY | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall ensure that the responsibilities and authorities of roles for information security are assigned and communicated. |  |  |
|  | Top management shall assign the responsibility and the authority for: <br> 1) Ensuring that the information security implemented in the entity conforms to the requirements of the UAE IA Standards <br> 2) Reporting on the performance of information security to top management |  |  |
| SUB-CONTROL | Top management shall ensure that <br> 3) An Information Security Manager is appointed to take overall responsibility for the establishment, implementation, maintenance and continual improvement of information security <br> 4) An Information Security Committee is established that oversees and governs the establishment, implementation, maintenance and continual improvement of information security in the entity, and that integrates information security in the entity |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The roles of the "Information Security Manager" and the "Information Security Committee" are important contributors to successful information security, and have therefore been defined as sub-controls. When implementing these sub-controls, please keep in mind that it is important to address these roles, but the name and way of implementation of these roles can be chosen by the entity. |  |  |  |
| The Information Security Committee should have a leading role for information security in the entity and should be responsible for handling the important information security issues. The members of the Information Security Committee should have a sufficient understanding of information security for directing, monitoring, and completing the necessary tasks. Typical tasks of an Information Security Committee could be: <br> A. Defining and establishing roles and responsibilities for information security <br> B. Monitor the adequacy of resources to maintain and improve information security in the entity and recommend to management the acquiring of additional resources where necessary <br> C. Providing input into the development, approval and implementation of information security policies and procedures |  |  |  |

--- Page 54 ---

D. Discussing practical issues regarding the implementation of information security policies and procedures and providing feedback from their respective parts of the entity
E. Ensure that the status of information security risks is up to date and approve the updated risk assessment
F. Recommending changes to policies and procedures based on security incidents and changes in risks
G. Deciding the criteria for accepting information security risks and the acceptable levels of risk
H. Identifying significant trends and changes to information security risks
I. Review the results of performance measurement activities
J. Reviewing audit reports and initiating appropriate corrective actions

The Information Security Manager should be the focal point for information security within the entity and should be responsible to direct the information security team (if present) and to provide valuable input into the Information Security Committee.

Additional responsibilities, such as technical security managers or asset owners can also be identified, as needed to implement information security in the entity. If necessary, roles and responsibilities should also be defined from contractors and third party users, and it should be ensured that all roles and responsibilities are reviewed periodically and kept up to date.

It is of particular importance that all people are aware of their responsibilities for information security and that everybody is aware of their duty to report information security incidents and events..

| M1.2 | INFORMATION SECURITY POLICY |
| :-- | :-- |
| OBJECTIVE | To provide a framework and management direction and support <br> for information security in the entity, in accordance with business <br> requirements and relevant laws and regulations. |
| PERFORMANCE <br> INDICATOR | Percentage of incidents that have been identified within the last <br> month, which are related to non-compliances with any of the existing <br> information security policies and procedures. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Breaches of information security <br> - Unawareness of policies and procedures <br> - Non-compliance with information security controls |

--- Page 55 ---

| M1.2.1 | INFORMATION SECURITY POLICY | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity's top management shall establish a policy for information security in the entity. |  |  |
| SUB-CONTROL | 1) Be appropriate to the purpose of the entity <br> 2) Provide the framework for setting information security objectives and/or include information security objectives (refer to M2.3.5) <br> 3) Include a commitment to satisfy all applicable information security requirements <br> 4) Include a commitment to continual improvement of the information security management system <br> 5) Be documented <br> 6) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| When developing the information security policy as well as the supporting policies (Control M1.2.2), take into account relevant NESA's issuances and guidance in this regard. |  |  |  |
| The following information should be considered for inclusion in the information security policy: <br> A. Statement related to management commitment and support of the goals and principles of information security in line with the business strategy and objectives <br> B. Description of the entity's approach to managing information security <br> C. Definition of information security in terms of confidentiality, integrity and availability <br> D. Reference to the entity risk management policy and the entity's approach to information security risk management <br> E. Reference to other risk management activities taking place in the entity, and how the information security risk management relates to that <br> F. Importance of compliance with the information security policy, and all supporting information security policies and procedures, and consequences of violations <br> G. Requirements of particular importance to the entity, e.g.: <br> - compliance with legislative, regulatory, sector and contractual requirements <br> - security education, training, and awareness requirements <br> - business continuity management <br> H. Definition of general and specific responsibilities for information security, including reporting information security incidents <br> I. References to supporting information security policies and procedures |  |  |
| This information security policy should be communicated throughout the entity in a form that is relevant, accessible and understandable to the intended reader. |  |  |  |
| The information security policy should be written in a way that it can also be communicated to outsiders, e.g. outsourcing partners or contractors. |  |  |  |

--- Page 56 ---

| M1.2.2 | SUPPORTING <br> POLICIES FOR <br> INFORMATION <br> SECURITY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall establish and communicate a set of supporting policies for information security |  |  |
| SUB-CONTROL | The set of supporting information security polices shall: <br> 1) Be defined, approved, published and communicated to employees and relevant external parties <br> 2) Address all aspects of information security that are included in this Standard, based on the risk assessment <br> 3) Address sector-specific regulations and standards <br> 4) Be suitable to the entity and shall have a clearly identified audience <br> 5) Reflect the implementation the entity has chosen and shall not include any statements the entity does not comply with <br> 6) Include commitment of the Top Management <br> 7) Be documented <br> 8) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The information security policy (refer to M1.2.1) should be supported by a set of supporting policies that address specific information security topics. Examples of topics to be addressed are: <br> A. Logical access control <br> B. Information classification and handling <br> C. Physical security <br> D. End user oriented topics such as: <br> - Acceptable use of assets <br> - Clear desk and clear screen <br> - Email and Internet <br> - Mobile devices <br> - Restrictions on software installations and use <br> - Media security <br> E. Backup \& recovery <br> F. Information exchange/sharing and transfer <br> G. Malware protection <br> H. Patch management <br> I. Cryptographic controls <br> J. Supplier relationships |  |  |  |
| These policies should be communicated to users in a form that is relevant, accessible and understandable to the intended reader, and sufficient training and awareness should be put in place to ensure that all users of these policies have understood and are aware of their content. It is also recommended to include the acceptance of compliance with all applicable policies and procedures in the induction process. |  |  |  |

--- Page 57 ---

| M1.3 | ORGANIZATION OF INFORMATION SECURITY |
| :-- | :-- |
| OBJECTIVE | To establish a management framework to initiate and control the <br> implementation of information security within the entity |
| PERFORMANCE <br> INDICATOR | Percentage of Top Management/Business Owners involved in the <br> Information Security program. Measure the percentage of strategic <br> information security decisions submitted and reviewed by the top <br> management. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Breaches of information security <br> - Unawareness of policies and procedures <br> - Non-compliance with information security controls <br> - Insufficient resources |


| M1.3.1 | AUTHORIZATION <br> PROCESS FOR <br> INFORMATION <br> SYSTEMS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |
| CONTROL | The entity shall establish a management authorization process for new <br> information systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define and implement a management authorization process for new <br> information systems <br> 2) Regulate the use of personal information systems for processing <br> business information |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

The following guidelines should be considered for the authorization process:
A. New facilities should have appropriate user management authorization, authorizing their purpose and use. Authorization should also be obtained from the manager responsible for maintaining the local information system security environment to ensure that all relevant security policies and requirements are met;
B. Where necessary, hardware and software should be checked to ensure that they are compatible with other system components;
C. The use of personal or privately owned information systems, e.g. laptops, home-computers or hand-held devices, for processing business information, may introduce new vulnerabilities and necessary controls should be identified and implemented.

--- Page 58 ---

| M1.3.2 | CONFIDENTIALITY <br> AGREEMENTS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall establish requirements for confidentiality or nondisclosure agreements reflecting the entity's needs for the protection of information. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a Non-Disclosure Agreement (NDA) template to be used to legally protect confidential information and ownership of information <br> 2) Have an information classification process in place to identify which information is subject to the terms of the NDA <br> 3) Keep a track record of all signed NDAs and perform a periodical review |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Confidentiality or non-disclosure agreements should address the requirement to protect confidential information using legally enforceable terms. To identify requirements for confidentiality or non-disclosure agreements, the following elements should be considered: <br> A. A definition of the information to be protected (e.g. confidential information); <br> B. Expected duration of an agreement, including cases where confidentiality might need to be maintained indefinitely <br> C. Required actions when an agreement is terminated <br> D. Responsibilities and actions of signatories to avoid unauthorized information disclosure (such as 'need to know') <br> E. Ownership of information, trade secrets and intellectual property, and how this relates to the protection of confidential information <br> F. The permitted use of confidential information, and rights of the signatory to use information <br> G. The right to audit and monitor activities that involve confidential information <br> H. Process for notification and reporting of unauthorized disclosure or confidential information breaches <br> I. Terms for information to be returned or destroyed at agreement cessation <br> J. Expected actions to be taken in case of a breach of this agreement |  |  |  |
| Based on an entity's security requirements, other elements may be needed in a confidentiality or non-disclosure agreement. |  |  |  |
| Confidentiality and non-disclosure agreements should comply with all applicable laws and regulations for the jurisdiction to which it applies. |  |  |  |
| Requirements for confidentiality and non-disclosure agreements should be reviewed periodically and when changes occur that influence these requirements. |  |  |  |

--- Page 59 ---

| M1.3.3 | CONTACT WITH <br> AUTHORITIES | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall maintain appropriate contacts with relevant authorities. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all relevant national authorities, including sector specific regulators <br> 2) Identify a Point of Contact in the Entity and communicate his/her name to the identified authorities, if required or allowed <br> 3) Establish a policy to determine when and how to engage relevant authorities |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Entities should have procedures in place that specify when and by whom authorities (e.g. law enforcement, fire department, supervisory authorities) should be contacted, and how identified information security incidents should be reported in a timely manner if it is suspected that laws may have been broken. (Refer to Information Security Events and Weaknesses Reporting T8.3). Entities under attack from the Internet may need external third parties (e.g. an Internet service provider or telecommunications operator) to take action against the attack source. Contact with authorities also could include external working groups. |  |  |  |  |


| M1.3.4 | CONTACT WITH SPECIAL INTEREST GROUPS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall maintain, as far as possible, appropriate contacts with relevant special interest groups. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all relevant national and international interest groups or working groups or other specialist security forums and professional associations <br> 2) Allocate the right resources in order to properly support the group <br> 3) Define what participating employees are allowed to share <br> 4) Allow sharing and circulation of information inside the entity, as permitted by interest group rules |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Membership in special interest groups or forums should be considered as a means to: <br> A. Improve knowledge about best practices and staying up to date with relevant security information <br> B. Ensure the understanding of the information security environment is current and complete <br> C. Receive early warnings of alerts, advisories, and patches pertaining to attacks and vulnerabilities <br> D. Gain access to specialist information security advice <br> E. Share and exchange information about new technologies, products, threats, or vulnerabilities <br> F. Provide suitable liaison points when dealing with information security incidents |  |  |  |  |

--- Page 60 ---

| M1.3.5 | IDENTIFICATION <br> OF RISKS RELATED TO EXTERNAL PARTIES | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall identify and properly manage the risks related to its information and information systems from business processes involving external parties |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify risks to its information and information systems and implement the appropriate controls before granting access to any external party <br> 2) Define an external party access policy <br> 3) Identify and adopt proper controls to limit physical and logical access to information assets and entity information systems <br> 4) Monitor external party access to entity information and entity information systems |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Where there is a need to allow an external party access to the information systems or information of an entity, a risk assessment should be carried out to identify any requirements for specific controls. The identification of risks related to external party access should take into account the following issues: <br> A. The information systems an external party is required to access <br> B. The type of access the external party will have to the information and information systems, e.g. <br> 1- Physical access, e.g. to offices, computer rooms, filing cabinets <br> 2- Logical access, e.g. to an entity's databases, information systems <br> 3- Network connectivity between the entity's and the external party's network(s), e.g. permanent connection, remote access <br> 4- Whether the access is taking place on-site or off-site <br> C. The value and sensitivity of the information involved, and its criticality for business operations <br> D. The controls necessary to protect information that is not intended to be accessible by external parties <br> E. The external party personnel involved in handling the entity's information <br> F. How the entity or personnel authorized to have access can be identified, the authorization verified, and how often this needs to be reconfirmed <br> G. The different means and controls employed by the external party when storing, processing, communicating, sharing and exchanging information <br> H. The impact of access not being available to the external party when required, and the external party entering or receiving inaccurate or misleading information <br> I. Practices and procedures to deal with information security incidents and potential damages, and the terms and conditions for the continuation of external party access in the case of an information security incident <br> J. Legal and regulatory requirements and other contractual obligations relevant to the external party that should be taken into account <br> K. How the interests of any other stakeholders may be affected by the arrangements |  |  |
| Access by external parties to the entity's information should not be provided until the appropriate controls have been implemented and, where feasible, a contract has been signed defining the terms and conditions for the connection or access and the working arrangement. Generally, all security requirements resulting from work with external parties or internal controls should be reflected by the agreement with the external party. It should be ensured that the external party is aware of their obligations, and accepts the responsibilities and liabilities involved in accessing, processing, communicating, or managing the entity's information and information systems. |  |  |  |

--- Page 61 ---

| M1.3.6 | ADDRESSING SECURITY WHEN DEALING WITH CUSTOMERS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall address all identified security requirements before giving customers access to the entity's information or assets. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) make sure that any customer accessing entity information and information systems are compliant with the entity's information security policy and security requirements <br> 2) monitor any customer access and verify compliance to agreed access control policy |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following terms should be considered to address security prior to giving customers access to any of the entity's assets (depending on the type and extent of access given, not all of them might apply): <br> A. Asset protection, including: <br> 1- Procedures to protect the entity's assets, including information and software, and management of known vulnerabilities <br> 2- Procedures to determine whether any compromise of the assets, e.g. loss or modification of data, has occurred <br> 3- Integrity <br> 4- Restrictions on copying and disclosing information <br> B. Description of the product or service to be provided <br> C. The different reasons, requirements, and benefits for customer access <br> D. Access control policy, covering <br> 1- Permitted access methods, and the control and use of unique identifiers such as user IDs and passwords <br> 2- An authorization process for user access and privileges <br> 3- A statement that all access that is not explicitly authorized is forbidden <br> 4- A process for revoking access rights or interrupting the connection between systems <br> E. Arrangements for reporting, notification, and investigation of information inaccuracies (e.g. of personal details), information security incidents and security breaches; <br> F. A description of each service to be made available <br> G. The target level of service and unacceptable levels of service <br> H. The right to monitor, and revoke, any activity related to the entity's assets <br> I. The respective liabilities of the entity and the customer <br> J. Responsibilities with respect to legal matters and how it is ensured that the legal requirements are met, e.g. data protection legislation, especially taking into account different national legal systems if the agreement involves co-operation with customers in other countries <br> K. Intellectual property rights (IPRs) and copyright assignment and protection of any collaborative work |  |  |

--- Page 62 ---

| M1.3.7 | ADDRESSING SECURITY IN THIRD PARTY AGREEMENTS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall have agreements that cover all relevant security requirements with third parties to handle the entity's information assets |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Verify that any contract or agreement with third parties addresses all aspects of the entity's information security policy regarding accessing, processing, communicating or managing the entity's information or information systems, or adding products or services to information systems <br> 2) Make sure that proper controls are introduced in the contract in order to verify compliance with the agreed security objectives (refer to T6) <br> 3) Perform audit of third parties services and infrastructures to verify compliance with agreed security objectives |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The agreement should ensure that there is no misunderstanding between the entity and the third party. Entities should satisfy themselves as to the indemnity of the third party. |  |  |  |
| The following terms should be considered for inclusion in the agreement in order to satisfy the identified security requirements: <br> A. The information security policy <br> B. Controls to ensure asset protection, including: <br> 1- Procedures to protect organizational assets, including information, software and hardware <br> 2- Any required physical protection controls and mechanisms <br> 3- Controls to ensure protection against malicious software <br> 4- Procedures to determine whether any compromise of the assets, e.g. loss or modification of information, software and hardware, has occurred <br> 5- Controls to ensure the return or destruction of information and assets at the end of, or at an agreed point in time during, the agreement <br> 6- Confidentiality, integrity, availability, and any other relevant property of the assets <br> 7- Restrictions on copying and disclosing information, and using confidentiality agreements <br> C. User and administrator training in methods, procedures, and security <br> D. Ensuring user awareness for information security responsibilities and issues <br> E. Provision for the transfer of personnel, where appropriate <br> F. Responsibilities regarding hardware and software installation and maintenance <br> G. A clear reporting structure and agreed reporting formats <br> H. A clear and specified process of change management |  |  |

--- Page 63 ---

I. Access control policy, covering:
1- The different reasons, requirements, and benefits that make the access by the third party necessary
2- Permitted access methods, and the control and use of unique identifiers such as user IDs and passwords
3- An authorization process for user access and privileges
4- A requirement to maintain a list of individuals authorized to use the services being made available, and what their rights and privileges are with respect to such use
5- A statement that all access that is not explicitly authorized is forbidden;
6- A process for revoking access rights or interrupting the connection between systems
J. Arrangements for reporting, notification, and investigation of information security incidents and security breaches, as well as violations of the requirements stated in the agreement
K. A description of the product or service to be provided, and a description of the information to be made available along with its security classification
L. The target level of service and unacceptable levels of service
M. The definition of verifiable performance criteria, their monitoring and reporting
N. The right to monitor, and revoke, any activity related to the entity's assets
O. The right to audit responsibilities defined in the agreement, to have those audits carried out by a third party, and to enumerate the statutory rights of auditors
P. The establishment of an escalation process for problem resolution
Q. Service continuity requirements, including measures for availability and reliability, in accordance with an entity's business priorities
R. The respective liabilities of the parties to the agreement
S. Responsibilities with respect to legal matters and how it is ensured that the legal requirements are met, e.g. data protection legislation, especially taking into account different national legal systems if the agreement involves co-operation with entities in other countries
T. Intellectual property rights (IPRs) and copyright assignment and protection of any collaborative work
U. Involvement of the third party with subcontractors, and the security controls these subcontractors need to implement
V. Conditions for renegotiation/termination of agreements:

1- A contingency plan should be in place in case either party wishes to terminate the relation before the end of the agreements
2- Renegotiation of agreements if the security requirements of the entity change
3- Current documentation of asset lists, licenses, agreements or rights relating to them

--- Page 64 ---

| M1.4 | SUPPORT |
| :--: | :--: |
| OBJECTIVE | To provide sufficient resources, appropriate communication and documentation for the Entity Information Security Program. |
| PERFORMANCE <br> INDICATOR | Percentage of incidents that are caused by a lack of qualified resources for information security. |
| AUTOMATION GUIDANCE | Not applicable |
| RELEVANT THREATS AND VULNERABILITIES | - Insufficient resources <br> - Non-compliance with information security controls <br> - Incompetent information security personnel <br> - Incomplete or not up to date documentation |
| M1.4.1 | RESOURCES PRIORITY <br> APPLICABILITY P1 <br> ALWAYS APPLICABLE |
| CONTROL | The entity shall determine and provide the appropriate resources needed for the entity's information security continual improvement |
| SUB-CONTROL | The entity shall ensure for the establishment, implementation, maintenance and continual improvement of its information security that: <br> A The amount of human and financial resources provided shall be adequate for the work to be carried out for information security <br> B The allocated human resources shall be sufficiently competent for their information security roles and responsibilities; the entity shall: <br> 1- Determine the necessary competence of person(s) doing work under its control that affects its information security performance <br> 2- Ensure that these persons are competent on the basis of appropriate education, training, or experience <br> 3- Where applicable, take actions to acquire the necessary competence, and evaluate the effectiveness of the actions taken <br> 4- Retain appropriate documented information as evidence of competence |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |
| The entity should allocate appropriate resources for information security, taking account of: <br> A. people, skills, experience and competence <br> B. Resources needed for each part of the process to achieve and maintain information security <br> C. Specific resources for information security risk management (refer to M2) <br> D. Documentation (refer to M1.4.3) <br> E. Knowledge and management of competence <br> F. Training programs (refer to M3.2) <br> Top management is responsible for ensuring that the right resources are allocated, and that all resources receive appropriate training. All personnel should have the competence to perform the operations required in the role assigned. The training performed should help all personnel be aware of and understand the meaning and importance of the information security activities they are involved in, and how they can contribute to achieving the objectives of information security. |  |

--- Page 65 ---

| M1.4.2 | INTERNAL AND <br> EXTERNAL <br> COMMUNICATION | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL

SUB-CONTROL

The entity shall determine the plan and mechanism for internal and external communications in support of its information security.

1) The entity shall determine:
A. On what to communicate
B. When to communicate
C. With whom to communicate
D. Who shall communicate
E. The processes by which communication shall be effected
2) The entity shall ensure that adequate communication can be maintained with the designated UAE Government entities
3) The entity shall document the communication plan.

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
INTERNAL COMMUNICATION: The entity should establish internal communication and reporting mechanisms in order to support information security. These mechanisms should ensure that:
A. Key components of the information security controls, and any subsequent modifications, are communicated appropriately
B. There is adequate internal reporting on information security, its effectiveness and the outcomes
C. Relevant information derived from the application of security controls is available in the entity, as appropriate
D. There are processes for consultation with internal stakeholders

EXTERNAL COMMUNICATION: The entity should develop and implement a plan as to how it will communicate with external stakeholders. This should involve:
A. Engaging appropriate external stakeholders and ensuring an effective exchange of information)
B. External reporting to comply with legal, regulatory, sector and governance requirements;
C. Providing feedback and reporting on communication and consultation
D. Using communication to build confidence in the entity and its security
E. Communicating with stakeholders in the event of a crisis or contingency

During communication, care should be taken regarding the confidentiality of the information involved.

--- Page 66 ---

| M1.4.3 | DOCUMENTATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall maintain, protect and control documentation of its information security controls and their implementation. |  |  |
| SUB-CONTROL | The entity shall ensure that: <br> 1) Documents are approved prior to issue <br> 2) Documents are reviewed and updated as necessary <br> 3) Changes and the current revision status of documents are identified <br> 4) Documents remain legible and readily identifiable <br> 5) Documents are available to those who need them, are transferred, and stored in accordance with the procedures applicable to their classification <br> 6) Documents are disposed of in accordance with the procedures applicable to their classification <br> 7) Documents of external origin are identified <br> 8) The distribution of documents is controlled <br> 9) The unintended use of obsolete documents is prevented, and that up to date versions are available <br> 10) Suitable identification is applied to documents if they are retained for any purpose <br> The entity shall document the compliance with the "mandatory" controls in a way that allows unique reference to the requirements of this Standard. (Sample Compliance Template may be provided by NESA in this regard). |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| One of the most important aspects of implementing document management in an entity is to do this consistent and throughout the entity, with supporting training, awareness and also checking that the document management controls are followed. It is necessary to include templates for document management in all documentation, irrespective of the form it takes. <br> All this can be supported by using document management systems and other controls to technically ensure that the necessary actions are carried out, wherever it is possible, it is recommended to use technical support to achieve a complete implementation. <br> Compliance with this control should be checked every so often, and non-compliances should be reacted to, to demonstrate that this actually is an important control everybody needs to comply with. <br> Particular attention should be given to the protection of records - it is not so important for records to have an author (they are often system based- and a change history (they should not change at all if they are supposed to provide evidence), but the date of issue and the integrity of the record are important items to maintain. |  |  |  |

--- Page 67 ---

# M2 INFORMATION SECURITY RISK MANAGEMENT 

| M2 | INFORMATION SECURITY RISK MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that information security risks in the entity are identified, <br> assessed and -evaluated, and that these risks are treated in <br> accordance with the information security requirements and <br> objectives of the entity |
| PERFORMANCE <br> INDICATOR | Measure the percentage of risks that appear in the previous and the <br> current risk assessment that have changed to a lower level. <br> Percentage of risks that appear in the previous and the current risk <br> assessment that have changed to a higher level |
| M2.1 | INFORMATION SECURITY RISK MANAGEMENT POLICY |
| OBJECTIVE | To establish a formal information risk management framework for <br> managing entity's information security risks by establishing the <br> context, preforming risk assessment, implementing risk treatments, <br> and monitoring their implementation |
| PERFORMANCE <br> INDICATOR | Trend in the number of occurrences where the risk assessment has <br> not been performed, reviewed or updated as planned. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT THREATS <br> AND VULNERABILITIES | - Unsuitable risk management policy <br> - Inconsistent or incomparable results <br> - Inconsistent or unsuitable risk criteria |

--- Page 68 ---

| M2.1.1 | INFORMATION SECURITY RISK MANAGEMENT POLICY | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall establish a formal information security risk management policy. |  |  |
| SUB-CONTROL | The information security risk management policy shall: <br> 1) Take into account relevant NESA's issuances in regard to risk management <br> 2) Be documented and formally approved <br> 3) Addresses the purpose and scope of critical services and their supporting functions <br> 4) Categorize Information Asset based on its criticality <br> 5) Addresses roles and responsibilities of the risk assessment team involved <br> 6) Establish and maintain information security basic criteria, including the risk acceptance criteria, impact criteria, and risk evaluation criteria <br> 7) Contain a risk treatment strategy <br> 8) Contain a risk monitoring and review strategy <br> 9) Determine the criteria for performing, reviewing and updating information security risk assessments <br> 10) Ensure that repeated information security risk assessments produce consistent, valid and comparable results |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Entities owning, operating, and or maintaining Critical Information Infrastructure shall take into account all relevant NESA's issuances and guidance with regard to risk management when performing risk assessment (Please refer to NCRMF for further details). |  |  |  |
| The information security risk management policy should clearly define how the entity is planning to carry out the risk assessment. In addition to the requirements stated above, the policy can, for example, contain: <br> A. The level of detail of asset identification <br> B. The basis of threat and vulnerability identification <br> C. The scales to be used for asset valuation in terms of confidentiality, integrity and availability <br> D. How the likelihood that a threat exploits a vulnerability is calculated <br> E. How the risks are calculated <br> F. Who will be responsible to perform the risk assessment <br> G. The basis of control selection <br> H. How to measure the risk management performance <br> I. Criteria for improving the risk management |  |  |  |

--- Page 69 ---

The risk management policy should also describe the type of risk assessment the entity intends to perform, whether it is more of a higher level assessment or a detailed one (see also M2.2), and the reasons for that choice. The decision for a particular approach should be made based on
A. The security requirements of the entity
B. Their current level of maturity, and where the entity eventually wishes to be (link to self-assessment)
C. The capabilities, knowledge and resources available at this point in time
D. The regulations given by the entity's sector or other applicable regulations

The entity should be able to provide reasons for the chosen information security risk management approach.

The risk management policy should be communicated appropriately.

PLEASE NOTE: The risk management policy is sometimes also denoted as risk management approach.

# M2.2 

## INFORMATION SECURITY RISK ASSESSMENT

OBJECTIVE

PERFORMANCE
INDICATOR

AUTOMATION
GUIDANCE

RELEVANT
THREATS AND
VULNERABILITIES

To identify, analyze and evaluate the information security risks the entity is facing.

Percentage of new risks that are identified when the risk assessment is reviewed or updated in relation to all those risks that should have been identified before and have been overlooked or that have been assessed incorrectly.

Tools can be used for risk assessment and treatment; there are many tools on the market. When doing so, care should be taken to use a tool that is

- Suitable to the entity
- Complies with the requirements of these Standards
- Allows to address all controls included in these Standards
- Easy and effective to use

The use of risk assessment tools can help in performing and updating the risk assessment and treatment.

- Unidentified risks
- Incorrect asset valuation
- Threats or vulnerabilities that have not been considered
- Wrongly assessed risks

--- Page 70 ---

| M2.2.1 | INFORMATION SECURITY RISK IDENTIFICATION | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall identify its information security risks. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Apply the information security risk assessment process to identify risks associated with the loss of confidentiality, integrity and availability for its information by: <br> - Define the scope of the risk assessment exercise <br> - Identify critical business functions <br> - Identify critical information systems supporting business critical functions within the scope and boundary of the risk assessment <br> - Identifying vulnerabilities related to the information and information systems. (see also T 7.7) <br> - Identify existing information security controls <br> - Identifying threats and threat sources <br> 2) Identify the risk owners <br> 3) Document the results of the risk identification. |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| There is a lot of information related to the performance of information security risk assessments; therefore, this implementation guidance will just provide an overview of the most important concepts. Entities should take into account relevant NESA's issuances and guidance with regard to risk management when performing risk assessment. |  |  |  |
| LEVEL OF DETAIL OF THE INFORMATION SECURITY RISK ASSESSMENT |  |  |  |
| Some entities might find it difficult or time consuming to conduct a detailed risk assessment. The choice of a suitable risk management approach should be taken when drafting the Information Security Risk Management Policy (refer to M2.1.1), and the implementation guidance there explains the considerations the entity should take into account when deciding on a suitable way of doing information security risk management. The entity should document these results and should be able to provide reasons for the decision taken. |  |  |  |
| An entity will only be considered as being compliant with the requirements of this Standard if they apply a suitable information security risk management policy. |  |  |  |

--- Page 71 ---

# ASSET IDENTIFICATION 

The assets to be considered in the information security risk assessment are all information assets, i.e. include:
A. INFORMATION: Databases, files, contracts and agreements, system documentation, research information, user manuals, training material, operational or support procedures, etc.
B. SOFTWARE ASSETS: Application software, system software, development tools, and utilities
C. PHYSICAL ASSETS: Computer equipment, communications equipment, removable media
D. OTHER EQUIPMENT
E. SERVICES: Computing and communications services, general utilities, e.g. heating, lighting, power, and air-conditioning
F. PEOPLE, and their qualifications, skills, and experience
G. INTANGIBLES, such as reputation and image of the entity

The identified assets are summarized in the Asset Inventory (refer to T1.2.1).
It might be useful to summarize assets in suitable groups (e.g. all PCs in a call center, processing the same type of information), but care should be taken to only group "like with like" when doing so. It is also helpful to take account of business processes, as they often can help to understand the information flow and how assets are working in the entity.

## IDENTIFICATION OF THREATS

Threats are not very dependent on the entity and its business; they are just out there trying to succeed. When identifying threats, it can be helpful to use threat lists (e.g. those provided in this Standard, or in other standards, such as ISO/IEC 27005), and to look into incident reports (incidents are always related to threats that have been successful- and audit reports, and to keep an open mind to the latest development as new threats will continue to emerge. It is also important to not only look at threats from the outside, such as hackers or malware, but also consider inside threats. A disgruntled employee with given access rights can often do more damage as outsiders.

## IDENTIFICATION OF VULNERABILITIES

The identification of vulnerabilities should be based on an assessment of the existing controls. To do so, it is recommended to conduct a gap analysis, which checks the controls in place against this Standard. The results of the gap analysis form an input in the identification of vulnerabilities as well as into the assessment of the risk likelihood (see also M2.2.2 below). Any control, which has been identified as missing, not completely in place, not fully documented or not complied with identifies at least one (if not more- vulnerabilities, which might be exploited by the identified threats.

PLEASE NOTE: The identification of threats and vulnerabilities takes place per each identified asset, so this easily produces a lot of information. To keep the amount of information manageable, it is recommended to:
A. Identify threats and vulnerabilities with the existing controls in mind
B. Identify only threat/vulnerability pairs where the threat will actually exploit the vulnerability See also T 7.7 on Technical Vulnerability Management

--- Page 72 ---

| M2.2.2 | INFORMATION SECURITY RISK ANALYSIS | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall analyze its information security risks. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Assess the potential consequences that would result if the identified risks were to materialize by assessing the consequences of losses of confidentiality, integrity or availability <br> 2) Assess the realistic likelihood of the occurrence of the identified risks based on the existing controls, identified vulnerabilities and threats <br> 3) Determine the levels of risk <br> 4) Document the results of the risk analysis |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| There is a lot of information related to the performance of information security risk assessments, and more details will be provided in a separate risk management document, therefore, this implementation guidance will just provide an overview of the most important concepts. |  |  |  |
| Consequences of losses of confidentiality, integrity or availability: The first part of assessing the consequences of losses of confidentiality, integrity or availability is to identify the business importance the information asset under consideration has. Damage to an asset that is important for the business is much likelier to cause severe consequences than an asset that is not as important. Based on the business use of the asset, the consequences for a loss of the following needs to be assessed: <br> A. CONFIDENTIALITY - This means the information asset is only accessible to those authorized to access it <br> B. INTEGRITY - This means the information asset has not been modified in any unauthorized way <br> C. AVAILABILITY - This means the information asset is available, when needed |  |  |  |
| To make the results of this assessment comparable, scales should be used, which should have been defined in the Information Security Risk Management Policy (see M2.1.1 above). |  |  |  |
| The assessment of these consequences should be done together with the business users of the information assets, as these can give important input into the process because they are aware of the security requirements for their assets. This can be done by interviews and/or questionnaires, but it is important to ensure that the business users understand what is asked from them. |  |  |  |
| As a result, each asset should have identified consequences of losses of confidentiality, integrity and availability.. |  |  |  |

--- Page 73 ---

# LIKELIHOOD OF THREAT/VULNERABILITY COMBINATIONS 

The input into the assessment of the likelihood that a particular threat exploits a vulnerability is based on very similar considerations as the identification of threats and vulnerabilities (see M2.2.1 above). The likelihood of a threat occurring can be derived from threat catalogues and statistics, as well as incident records, audit logs and reports, etc. the entity has produced.

The level of vulnerability is based on how good or bad the controls are that have been put in place, so this can also be derived from the results of the gap analysis (see M2.2.1 above). Finally, the likelihood of the threat to occur and the level of vulnerability are put together to determine the likelihood that this particular threat/vulnerability combination occurs. How exactly these values are put together has been defined in the Information Security Risk Management Policy (see M2.1.1. above).

Determining the levels of risk: Based on the method to calculate risks, which has been chosen by the entity and has been documented in the Information Security Risk Management Policy (see M2.1.1. above), the risks should now be calculated using the consequences and likelihoods that have been assessed.

PLEASE NOTE: The details on how to calculate the risks and which valuation schemes are used for consequences and likelihood is entirely up to the entity to decide. It is nevertheless important that the approach chosen is applied consistently.

--- Page 74 ---

| M2.2.3 | INFORMATION SECURITY RISK EVALUATION ANALYSIS | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall evaluate its information security risks. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Compare the analyzed risks with the risk criteria established in the information security risk management policy (See M2.1.1) <br> 2) Establish priorities for treatment of the identified risks <br> 3) Document the results of the risk evaluation and share with national and sector authorities, as required |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| There is a lot of information related to the performance of information security risk assessments, and more details will be provided in a separate risk management document, therefore, this implementation guidance will just provide an overview of the most important concepts. |  |  |  |
| Once the risks have been calculated (see M2.2.2 above), the entity should compare the risk levels assessed with the risk criteria that have been established documented in the Information Security Risk Management Policy (see M2.1.1. above). This will rank the risks in order of severity and will identify those that are acceptable (because they are below the general threshold of acceptance), and those risks that will require treatment. |  |  |  |
| If necessary, the entity can assign additional priorities to the risks, e.g. if a risk - despite of not being high- relates to a very vital business process. Any such assignment is entirely up to the entity, any decisions made should be reasoned and documented. |  |  |  |
| Decisions on risks should take account of the wider context of the risk and include consideration of the requirements of other parties, such as sector, regional or national initiatives. In some circumstances, the risk evaluation can lead to a decision to undertake further analysis. |  |  |  |

--- Page 75 ---

| M2.3 | INFORMATION SECURITY RISK ASSESSMENT |
| :-- | :-- |
| OBJECTIVE | To identify and plan appropriate risk treatment for the risks that <br> have been assessed. |
| PERFORMANCE <br> INDICATOR | Percentage of all records (audit reports, incident reports, logs, <br> events, etc.) that indicate that any of the controls that have been <br> identified as "not applicable" are actually needed. |
| AUTOMATION <br> GUIDANCE | See M2.2 |
| RELEVANT THREATS <br> AND VULNERABILITIES | - Inadequately treated risks <br> - Incomplete control selection <br> - Too high residual risks <br> - Wrongly assessed residual risks <br> Lack of management awareness of information security risks |

--- Page 76 ---

| M2.3.1 | INFORMATION SECURITY RISK TREATMENT OPTIONS | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall select appropriate information security risk treatment options, taking account of the risk assessment results. |  |  |
| SUB-CONTROL | 1) The entity shall consider the following risk treatment options and select one or more of them for each of the risks that have been assessed: <br> - Risk Reduction - Reducing the risk by applying security controls <br> - Risk Retention - Accepting the risk based on the entity's risk accepting criteria established on the information management risk policy (See M2.1.1) <br> - Risk Avoidance - Avoiding the activity or condition causing the risk <br> - Risk Transfer - Transferring the risk to another party <br> 2) The entity shall assess the risk treatment chosen to ensure that the selection of risk treatment options is successful by: <br> - Deciding whether residual risk levels are tolerable <br> - If not tolerable, generating a new risk treatment <br> - Assessing the effectiveness of that treatment (see also M2.3) |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Selecting the most appropriate information security risk treatment option involves balancing the costs and efforts of implementation against the benefits derived, with regard to sector, national or regulatory requirements. Decisions should also take into account risks which can warrant risk treatment that is not justifiable on economic grounds, e.g. severe (high negative consequence- but rare (low likelihood- risks. <br> A number of treatment options can and should be considered and applied either individually or in combination. When selecting risk treatment options, the entity should consider the expectations of the sector and national level. Though equally effective, some risk treatments can be more acceptable to some stakeholders than to others. <br> The selected risk treatment options should be documented in the risk treatment plan. The treatment plan should clearly identify the priority order in which individual risk treatments should be implemented. <br> Risk treatment itself can introduce risks. A significant risk can be the failure or ineffectiveness of the risk treatment measures. Monitoring needs to be an integral part of the risk treatment plan to give assurance that the measures remain effective (see also M6). |  |  |  |

--- Page 77 ---

| M2.3.2 | IDENTIFICATION OF CONTROLS | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall identify all controls that are necessary to implement the information security risk treatment option(s) chosen. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Consider the controls included in these Standards as a starting point for the control identification <br> 2) Ensure that no controls are overlooked by producing the Statement of Applicability (refer to M2.3.4) <br> 3) Identify controls in addition to the controls suggested in this Standard that are specific to the entity <br> 4) Take account of the criteria for accepting risks (refer to M2.3.1) as well as legal, regulatory and contractual requirements when making the control selection. |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Controls should be identified to manage the risks, based on the identified risk treatment option(s). It is important to specify the relation between the risks and the identified controls, this relation is important for the ongoing risk management and should be documented in the risk treatment plan. <br> The first basis of control identification should be this Standard, which suggests a set of "riskbased applicable" controls that addresses a lot of the common information security risks. Sector-specific controls should be identified to support the specific needs of the entity within its sector. <br> The entity should also identify controls that are required for risk management and not documented in this Standard. It is likely that such controls exist as an entity has risks specific to its business and its way to operate, and the identification of additional controls completes the controls for information security risk management. <br> The entity should compile a list of controls which have been identified to produce a Statement of Applicability (refer to M2.3.4). It might be that the Statement of Applicability (refer to Implementation Guidance of M2.3.4) leads to a revision of the identified controls. This is the intention of producing the Statement of Applicability, it is supposed to act as a safety net that ensures that no impotent control has been overlooked. <br> It is important to be aware of that the list of identified controls is very likely to contain sensitive information. Therefore, appropriate care should be taken when making the summary of controls available to both internal and external recipients. |  |  |  |

--- Page 78 ---

| M2.3.3 | RISK TREATMENT <br> PLAN | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL The entity shall formulate a risk treatment plan..

SUB-CONTROL

1) The risk treatment plan shall identify:
A. Appropriate management actions
B. Resources required
C. Responsibilities and priorities for managing information security risks
D. Target dates for implementation of the identified controls
2) The entity shall document the risk treatment plan.

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

The purpose of risk treatment plans is to document how the chosen risk treatment options will be implemented. The information provided in treatment plans should include:
A. The reasons for selection of treatment options
B. The controls that have been identified to implement the selected risk treatment option(s)
C. The identified risk reduction or other modification that is intended to be achieved by the identified control(s), also called residual risk
D. Those who are accountable for approving the plan
E. Those responsible for implementing controls and the overall plan
F. Proposed actions to achieve this implementation
G. Priorities of implementation
H. Resource requirements including contingencies
I. Target dates for control implementation
J. Interdependencies of control implementation (when the implementation of a control requires the complete implementation of another control)
K. Performance measures and constraints (which can also be documented elsewhere); and
L. Reporting and monitoring requirements

The risk treatment plan should be integrated with the management processes of the entity and discussed with appropriate stakeholders.

Management should be aware of the nature and extent of the residual risk after risk treatment and should accept the residual risks. The residual risk should be documented and subjected to monitoring, review and, where appropriate, further treatment.

--- Page 79 ---

| M2.3.4 | STATEMENT OF APPLICABILITY | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL |  | The entity shall compare the controls identified in M2.3.2 above with the "risk-based applicable" controls contained in this Standard and shall verify that no necessary controls have been omitted. |  |
| SUB-CONTROL |  | The entity shall produce and document a Statement of Applicability that contains: <br> 1) The controls that have been identified as necessary <br> 2) Reasons for identification of these controls <br> 3) Their current status of implementation <br> 4) Justification for exclusion of any of the "risk-based applicable" controls contained in these Standards |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
|  | The Statement of Applicability should be produced to ensure that no control from these Standards that is required by the entity for risk treatment is overlooked. <br> If the first version of the Statement of Applicability identifies controls from this Standard whose exclusion cannot be justified, the entity should go back to the control identification process (refer to M2.3.2) and check whether there are risks whose treatment could benefit from this control. If this is the case, the control under consideration should be included in the risk treatment. If this is not the case, the entity should go back to the risk identification and ensure that all important risks have been identified. <br> The reasons for the identification of controls is needed to form the link between risks and controls - this relationship can also be documented in the risk treatment plan (refer to M2.3.3). The Statement of Applicability can be a separate document, or can be combined with the risk treatment plan, this can be decided by the entity. |  |  |  |

--- Page 80 ---

|  M2.3.5 | INFORMATION SECURITY OBJECTIVES | PRIORITY | P2  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | ALWAYS APPLICABLE  |
|  CONTROL | The entity shall establish information security objectives at relevant to its functions and levels. |  |   |
|  SUB-CONTROL | 1) The information security objectives shall:
A. Be consistent with the information security policy
B. Be measurable (if practicable)
C. Take into account applicable information security requirements, and risk assessment and treatment results
D. Be communicated within the entity
E. Be updated as appropriate
F. Be documented |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  Based on the business objectives for information security and the results of the information security risk assessment and risk treatment process, information security objectives should be identified. The entity can consider high level objectives, such as:
A. Maintaining the confidentially of sensitive entity information
B. Successful management of the information security risks
C. Efficient management of information security in the entity
D. Compliance with sector or national requirements |  |  |   |
|  These high level information security objectives are often directly derived from the business objectives, and other, lower level objectives, can be identified to support their fulfillment. The lower level information security objectives can be identified based on the results of the information security risk assessment and risk treatment process, and can also be identified by considering the following questions:
A. What third party relationships and agreements exist, and what are associated information security requirements?
B. Are there any services that have been outsourced?
C. What kind of protection is needed, and against what threats?
D. What are the distinct categories of information that require protection?
E. What are the distinct types of information activities that need to be protected?
F. What are the minimum market requirements for information security?
G. What additional information security controls should provide a competitive advantage for the entity?
H. What are the critical business processes, and how long can the entity tolerate interruptions to each critical business process? |  |  |   |
|  When planning how to achieve the information security objectives, it can be helpful to develop an equivalent of the risk treatment plan, i.e. a plan that details the actions, resources, responsibilities, time frames and methods of evaluating whether the objectives have been achieved. |  |  |   |
|  When planning how to achieve its information security objectives, the entity shall determine:
A. What will be done
B. What resources will be required
C. Who will be responsible
D. When it will be completed
E. How the results will be evaluated |  |  |   |

--- Page 81 ---

| M2.4 | ONGOING INFORMATION SECURITY RISK MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that risk management process is communicated, <br> consulted and monitored. |
| PERFORMANCE <br> INDICATOR | Percentage of all cases during the last year where the information <br> security risk assessment and/or risk treatment has not been <br> updated despite of being scheduled and significant changes are <br> occurring |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT THREATS <br> AND VULNERABILITIES | - No review or update of the information security risk assessment <br> and treatment <br> - Unidentified new information security risks <br> - Unnecessary controls |


| M2.4.1 | RISK MONITORING AND REVIEW | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall plan and document the process for the review and update of the risk assessment and treatment; this shall include planned reviews and updates as well as ad hoc updates if significant changes occur. |  |  |
| SUB-CONTROL | 1) The entity's monitoring and review processes shall encompass all aspects of the risk management process and shall take account of changes in: <br> A. The entity itself <br> B. Technology used <br> C. Business objectives and processes <br> D. Risk criteria and the risk assessment process <br> E. Assets and consequences of losses of confidentiality, integrity or availability <br> F. Identified threats; <br> G. Identified vulnerabilities <br> H. Effectiveness of the implemented controls <br> I. External events, such as changes to the legal or regulatory environment, changed contractual obligations, and changes in social climate <br> 2) The entity shall monitor security incidents (see T8.3.2, T8.3.3) that might trigger the risk assessment process. (see M2.2.1) <br> 3) Responsibilities for monitoring and review shall be clearly defined and documented. |  |  |

--- Page 82 ---

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
Monitoring and review should be a planned part of the information security risk management process and involve regular checking, surveillance and updates. The monitoring should be an ongoing process, which identifies any changes that are relevant to information security risk management, and there should also be planned processes that ensure that risk assessment and treatment updates are taking place.

Responsibilities for monitoring and review should be clearly defined. (Refer to NCRMF for further details)

The entity's monitoring and review processes should encompass all aspects of the information security risk management process for the purposes of:
A. Ensuring that controls are effective in the risk management they are achieving
B. Integrating new information to improve the risk assessment and/or treatment
C. Analyzing and learning lessons from events (including near-misses), changes, trends, successes and failures;
D. Detecting changes in the external and internal context, including changes to risk criteria and the risk itself, which can require revision of risk treatments and priorities
E. Vulnerability Assessment should be conducted frequently even after implementing security controls to identify emerging risks, new threats, trends, etc.

Progress in implementing risk treatment plans provides a performance indicator in itself. The results can be incorporated into the entity's overall performance management, measurement and external and internal reporting activities.

The results of monitoring and review should be recorded and externally and internally reported as appropriate, and should also be used as an input to the review of the information security risk management policy (refer to M2.1.1).

--- Page 83 ---

| M2.4.2 | RISK <br> COMMUNICATION <br> AND <br> CONSULTATION | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL
The entity shall communicate and consult risk information obtained from risk management activities with all stakeholders involved.

SUB-CONTROL
The entity shall:

1) Establish a risk communication plan for communicating risk information with key stakeholders including decision-makers within the entity during all stages of the risk management process
2) Take into account all NESA's issuances with regard to risk management

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Communication and consultation with key stakeholders should take place during all stages of the risk management process. Therefore, plans for communication and consultation should be developed at an early stage. These should address issues relating to the risk itself, its causes, its consequences (if known), and the measures being taken to treat it. Effective external and internal communication and consultation should take place to ensure that stakeholders and those accountable for implementing the risk management process understand the basis on which decisions are made, as well as the reasons why particular actions are required.

--- Page 84 ---

# M3 AWARENESS AND TRAINING 

| M3 | AWARENESS AND TRAINING |
| :-- | :-- |
| OBJECTIVE | To ensure sufficient information security awareness and training is <br> provided and to build a specialized workforce |
| PERFORMANCE <br> INDICATOR | Percentage of awareness and training objectives that have been <br> met successfully |
| M3.1 | AWARENESS AND TRAINING POLICY |
| OBJECTIVE | To maintain an awareness and training policy outlining the approach <br> to identifying relevant topics, enrollment of stakeholders, and <br> documentation of activities |
| PERFORMANCE <br> INDICATOR | Trend in the number of employees that have not successfully <br> participated in the awareness and training program. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable awareness and training policy <br> - Non-comprehensive training identification approach <br> - Accidental information leaks due to lack of awareness <br> - Software malfunction due to lack of trained personnel |


| M3.1.1 | AWARENESS AND <br> TRAINING POLICY | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall develop and maintain an awareness and training policy.
SUB-CONTROL
The awareness and training policy shall:

1) Be appropriate to the purpose of the entity
2) Provide the framework for setting awareness and training objectives
3) Facilitate the implementation of the associated controls
4) Outline the roles and responsibilities of providers and recipients of awareness and training activities

## IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)

Critical entities shall also take into account NESA's relevant issuances, guidance, and activities with regards to National Awareness and Capability Building.

The policy document should contain statements concerning:
A. The purpose, scope, roles, responsibilities, management commitment, coordination among organizational entities, and compliance
B. The procedures to facilitate the implementation of the security awareness and training policy and associated security awareness and training controls
C. Factors to consider when awareness and training objectives are identified

--- Page 85 ---

| M3.2 | AWARENESS AND TRAINING PLANNING |
| :-- | :-- |
| OBJECTIVE | To ensure that all person(s) carrying out work effecting information <br> security are sufficiently aware of information security requirements and <br> controls, and are adequately competent. |
| PERFORMANCE <br> INDICATOR | Percentage of actions (planned training, participation in conferences, <br> etc.) that have not been carried out as planned. |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | Non-compliance with controls due to a lack of awareness <br> Not noticing security breaches <br> Incompetent information security personnel <br> Promoting a culture of disinterest in information security matters |


| M3.2.1 | AWARENESS <br> AND TRAINING <br> PROGRAM | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  | APPLICABILITY | ALWAYS APPLICABLE |  |
| CONTROL | The entity shall develop an awareness and training program. |  |  |
| SUB-CONTROL | The awareness and training program shall: <br> 1) Inform persons doing work under the entity of their contribution to <br> the effectiveness of information security and the implications of not <br> conforming to the information security requirements <br> The entity shall: <br> 2) Determine the necessary competencies for personnel performing <br> work effecting information security <br> 3) Provide training or taking other actions (e.g. employing competent <br> personnel) to satisfy these needs <br> 4) Evaluate the effectiveness of the actions taken <br> 5) Maintain records of education, training, skills, experience and <br> qualifications |  |  |

--- Page 86 ---

Critical entities shall also take into account NESA's national awareness and capability building issuances, guidance, and activities.

The entity should develop a program that ensures continued adequate awareness and competence for all persons doing work under the control of the entity. This does include not only entity personnel but also any outsiders with access to information. Please note that the implementation of the awareness and training program might not be carried out by the entity and can, for example, be ensured contractually.

The first step in the program is the evaluation of the competencies required for the job function. The Information Security Manager, for example, should have a good understanding of the controls contained in this standard, and should know how to implement them and to maintain them effectively.

The entity should ensure that trainings take place as planned, and are not pushed off, e.g. due to work overload. If such problems recur, it might be a sign for inadequate resourcing. If trainings continue not to take place in the time frame planned, it is a non-conformity to sub-control 2mentioned above.

The awareness and training program should ensure that records of all trainings are generated. These records should regularly be reviewed to ensure that all personnel have received the training that they require.

Whatever training is conducted, it is important that the effectiveness of this training is assessed. An easy way of such as assessment is to select trainings that include an exam at the end. Whenever this is not possible, interviews of feedback form should be used that provide enough information to be able to evaluate the effectiveness of the training.

| M3.3 | SECURITY TRAINING |
| :-- | :-- |
| OBJECTIVE | To ensure that all personnel who are assigned responsibilities in <br> information security are competent to perform the required tasks |
| PERFORMANCE <br> INDICATOR | Percentage of identified information security training requirements that <br> have been met with satisfactory results |
| AUTOMATION <br> GUIDANCE | Web-based training modules (internally or externally created) can be <br> used to implement trainings. This can also be used to automatically <br> update staff training records, as well as to capture CPE credits needed to <br> maintain security certifications. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Software malfunction due to lack of trained personnel <br> - Error in use due to undelivered training |

--- Page 87 ---

| M3.3.1 | TRAINING NEEDS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall identify its information security training needs. |  |  |
| SUB-CONTROL | The entity shall: |  |  |
|  | 1) Identify the information security skills needed within the entity <br> 2) Assess the current information skills in place within the entity <br> 3) Identify gaps between required and in place information security skills |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Entities determine the appropriate content of security training and techniques based on the <br> specific organizational requirements and the information systems to which personnel have <br> authorized access. The content includes a basic understanding of the need for information <br> security and user actions to maintain security and to respond to suspected security incidents. <br> The content should also include advanced security information for the implementation and <br> maintenance of information assets deployed within the entity. |  |  |  |


| M3.3.2 | IMPLEMENTATION <br> PLAN | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL The entity shall establish a clear plan to conduct the trainings needed for the corresponding target audience

SUB-CONTROL The entity shall:

1) Identify solutions for each information security training need that has been identified
2) Develop a timeline for delivering the information security training solutions
3) Ensure resources needed to execute information security training are allocated to the program

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Entities should determine the trainings that should be delivered, the medium (class based, web based, documents), the target audience, and develop the corresponding timeline for the execution in line with known organizational and users' constraints.

--- Page 88 ---

| M3.3.3 | TRAINING <br> EXECUTION | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL The entity shall conduct security training following an established plan.
SUB-CONTROL
The entity shall:

1) Ensure that information security training proceeds according to the implementation plan
2) Identify alternative information security training solutions if problems with the implementation plan arise
3) Ensure the updated implementation plan satisfies all of the information security training needs identified

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Security trainings typically focus on topics specific to the applications and systems within the entities, such as security best practices for implementing and maintaining a database or patching operating systems. Specific training methods may include:
A. Internal training websites
B. Manuals, guides, and handbooks
C. Slide presentations

Entities should update training based on changes within the IT landscape, such as changing technology, updated systems, new services, or new threats.

| M3.3.4 | TRAINING RESULTS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall measure and evaluate security training effectiveness. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Measure the level of information security knowledge and skills in the entity before and after the training plan is implemented <br> 2) Ensure that the information security training solutions implemented are meeting the expected outcomes against the knowledge requirements of the entity <br> 3) Take corrective action to improve or replace training solutions that are not reaching the expected outcome |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Effectiveness of training could be measured through: <br> A. Written individual assessment of the training <br> B. Voluntary self-reporting of participants <br> C. Interviews <br> D. Measurement of enhanced individual performance <br> E. Compare events and incidents in the entity with training provided |  |  |  |

--- Page 89 ---

| M3.3.5 | RECORDS <br> DOCUMENTATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall maintain training records of all security personnel. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Ensure that each target for information security training has a documented training record <br> 2) Ensure that all training activities are captured in the individual training records containing personnel education, training, skills, experience and qualifications <br> 3) Review training records periodically to ensure all stakeholders have completed the necessary training |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The entity should consider the following: <br> A. Document and monitor individual information system security training activities including basic security awareness training and specific information system security training <br> B. Retain individual training records in line with the training and awareness policy |  |  |  |


| M3.4 | SECURITY AWARENESS |
| :-- | :-- |
| OBJECTIVE | To foster security awareness of the workforce within the entity |
| PERFORMANCE <br> INDICATOR | Percentage of identified Information Security campaigns that have been <br> successfully implemented |
| AUTOMATION <br> GUIDANCE | Leverage internally or externally created web-based awareness modules <br> to allow recurring training by the general workforce and external <br> stakeholders. This can also be used to automatically update workforce <br> training records. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Successful pretexting due to lack of awareness <br> - Accidental leaks of data by staff <br> - Illegal processing of data |

--- Page 90 ---

| M3.4.1 | AWARENESS <br> CAMPAIGN | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall plan and conduct a security awareness campaign. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define the scope of the awareness campaign in terms of targets and content based on security risks relevant to users' activities <br> 2) Provide a timeline for deploying specific awareness campaigns to meet the program objectives <br> 3) Ensure that information security campaigns proceed according to the defined program timeline <br> 4) Identify alternative information security awareness campaigns if problems with the program timeline arise <br> 5) Ensure the updated information security awareness campaign satisfies all of the program objectives and needs identified |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Through awareness campaigns, the entity promotes a culture of security. Security awareness programs typically focus on broad topics, such as security threats that could be mitigated through good practice, the choice and usage of passwords, good practice for using a personal computer, sharing of account information, report incidents. <br> Entities determine the appropriate content of security awareness based on the specific organizational requirements and the information systems to which personnel have authorized access. Specific training methods may include: <br> A. Mandatory annual awareness training <br> B. Targeted, role-based training <br> C. Internal security awareness websites <br> D. Manuals, guides, and handbooks <br> E. Seminars and slide presentations <br> F. Events (e.g., security awareness week or month) <br> G. Posters and brochures <br> H. Email messages to all employees and contractors |  |  |  |
| Security awareness techniques can include, for example, displaying posters, offering supplies inscribed with security reminders, generating email advisories/notices from senior organizational officials, displaying logon screen messages, and conducting information security awareness events. |  |  |  |

--- Page 91 ---

# M4 HUMAN RESOURCES SECURITY 

| M4 | HUMAN RESOURCES SECURITY |
| :-- | :-- |
| OBJECTIVE | To ensure stakeholder awareness of information security threats as <br> well as their roles and responsibilities before, during and in post- <br> employment scenarios |
| PERFORMANCE <br> INDICATOR | Percentage of employees, contractors and third parties who read and <br> accepted human resources security policy |
| M4.1 | HUMAN RESOURCES SECURITY POLICY |
| OBJECTIVE | To maintain a human resources security policy covering the security <br> aspects of employment and termination, in addition to the inclusion of <br> information security in the job junction |
| PERFORMANCE <br> INDICATOR | Extent of HR security policy deployment and adoption across the entity <br> Number of employees, contractors and third parties who have accepted <br> the HR security policy and have denoted this acceptance in writing |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unawareness of the human resources security policy <br> - Non-compliance with human resources security policy <br> - Intentional leaks and sharing of data by staff |

--- Page 92 ---

| M4.1.1 | HUMAN <br> RESOURCES <br> SECURITY POLICY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall develop and maintain a human resources security policy and associated security controls. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish and maintain a human resources security policy that outlines roles and responsibilities of different stakeholders, and procedures to facilitate the implementation of the associated controls <br> 2) Identify and implement associated controls |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |
| The human resources security policy facilitates the implementation of the associated controls along the entire employment lifecycle: prior to employment, during employment, and termination or change of employment. The policy can, for example, contain: <br> A. Scope of the policy <br> B. Management roles and responsibilities during each phase of the employment lifecycle <br> C. Employment terms and conditions <br> D. Required information security awareness and training during employment in line with M3.1.1 <br> E. Employment termination procedures and checks |  |  |  |
| The human resources policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |


| M4.2 | PRIOR TO EMPLOYMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that employees, contractors and third party users understand <br> their responsibilities, and are suitable for the roles they are considered <br> for, and to reduce the risk of theft, fraud or misuse of facilities |
| PERFORMANCE <br> INDICATOR | Percentage of new employees and contractors that have been fully <br> screened and approved in accordance with company policies prior to <br> starting work |
|  | Percentage of employees, contractors and third parties who read and <br> accepted HR security policy |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Intentional leaks and sharing of data by staff <br> - Successful pretexting due to unsuitability of new employee <br> - Pretexting |

--- Page 93 ---

| M4.2.1 | SCREENING | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL |  | The entity shall perform background verification checks on all candidates for employment, contractors, and third party users |  |
|  | The entity shall: <br> 1) Define a background verification check process in accordance with relevant laws, regulations and ethics, and proportional to the business requirements, the classification of the information to be accessed, and the perceived risks <br> 2) Perform background verification checks for all candidates for employment, contractors and third party personnel |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Verification checks should take into account all relevant privacy, protection of personal data and/or employment based legislation, and should, where permitted, include the following: <br> A. Availability of satisfactory character references, e.g. one business and one personal <br> B. A check (for completeness and accuracy) of the applicant's curriculum vitae <br> C. Confirmation of claimed academic and professional qualifications <br> D. Independent identity check (passport or similar document) <br> E. More detailed checks, such as credit checks or checks of criminal records |  |  |  |
| Where a job, either on initial appointment or on promotion, involves the person having access to information systems, and in particular if these are handling sensitive information, e.g. financial information or highly confidential information, the entity should also consider further, more detailed checks. |  |  |  |
| Procedures should define criteria and limitations for verification checks, e.g. who is eligible to screen people, and how, when and why verification checks are carried out. |  |  |  |
| A screening process should also be carried out for contractors, and third party users. Where contractors are provided through an agency the contract with the agency should clearly specify the agency's responsibilities for screening and the notification procedures they need to follow if screening has not been completed or if the results give cause for doubt or concern. In the same way, the agreement with the third party should clearly specify all responsibilities and notification procedures for screening. |  |  |  |
| Information on all candidates being considered for positions within the entity should be collected and handled in accordance with any appropriate legislation existing in the relevant jurisdiction. Depending on applicable legislation, the candidates should be informed beforehand about the screening activities. |  |  |  |

--- Page 94 ---

| M4.2.2 | TERMS AND CONDITIONS OF EMPLOYMENT | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall ensure that employees, contractors and third party user understand, agree and sign the terms and conditions of their employment contract, which should state their and the entity's responsibilities for information security, as part of their contractual obligation. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define standard information security terms and conditions for employees, third parties and contractors <br> 2) Include information security terms and conditions in any contract <br> 3) Ensure that their employees, contractors, and third parties fully understand their relevant terms and conditions <br> 4) Review and eventually amend any existing contract with employees, contractors and third parties |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The terms and conditions of employment should reflect the entity's security policy in addition to clarifying and stating: <br> A. That all employees, contractors and third party users who are given access to sensitive information should sign a confidentiality or non-disclosure agreement prior to being given access to information systems <br> B. The employee's, contractor's and any other user's legal responsibilities and rights, e.g. regarding copyright laws or data protection legislation <br> C. Responsibilities for the classification of information and management of organizational assets associated with information systems and services handled by the employee, contractor or third party user <br> D. Responsibilities of the employee, contractor or third party user for the handling of information received from other companies or external parties <br> E. Responsibilities of the entity for the handling of personal information, including personal information created as a result of, or in the course of, employment with the entity <br> F. Responsibilities that are extended outside the entity's premises and outside normal working hours, e.g. in the case of home-working <br> G. Actions to be taken if the employee, contractor or third party user disregards the entity's security requirements |  |  |  |
| The entity should ensure that employees, contractors and third party users agree to terms and conditions concerning information security appropriate to the nature and extent of access they will have to the entity's assets associated with information systems and services. Where appropriate, responsibilities contained within the terms and conditions of employment should continue for a defined period after the end of the employment. |  |  |  |

--- Page 95 ---

| M4.3 | DURING EMPLOYMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that employees, contractors and third party users are aware <br> of information security threats and concerns, their responsibilities and <br> liabilities, and are equipped to support organizational security policy in <br> the course of their normal work, and to reduce the risk of human error |
| PERFORMANCE <br> INDICATOR | Percentage of employees that participated in Security Awareness Training |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Abuse of system access/privileges <br> - Use of unapproved hardware/devices <br> - Illegal processing of data |


| M4.3.1 | MANAGEMENT RESPONSIBILITIES | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity's management shall require employees, contractors and third party users to apply security in accordance with established policies and procedures of the entity. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Include in human resources security policy that employees, contractors and third party users have to comply with entity security policies and procedures <br> 2) Inform all employees, contractors and third parties of the security policies they are required to be compliant with <br> 3) Present, on first access, relevant security policy/guidelines for users to read and accept |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Management responsibilities should ensure that employees, contractors and third party users: <br> A. Are properly briefed on their information security roles and responsibilities prior to being granted access to sensitive information or information systems <br> B. Are provided with guidelines to state security expectations of their role within the entity <br> C. Are motivated to fulfill the security policies of the entity <br> D. Achieve a level of awareness on security relevant to their roles and responsibilities within the entity <br> E. Conform to the terms and conditions of employment, which includes the entity's information security policy and appropriate methods of working <br> F. Continue to have the appropriate skills and qualifications |  |  |  |

--- Page 96 ---

| M4.3.2 | DISCIPLINARY <br> PROCESS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL

SUB-CONTROL

The entity shall enforce a formal disciplinary process for employees who have committed a security breach.

The entity shall:

1) Define a formal disciplinary process
2) Ensure sufficient awareness about this disciplinary process within the entity
3) Enforce the disciplinary process
4) Keep records of the committed security breaches

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
The disciplinary process should not be commenced without prior verification that a security breach has occurred.

The formal disciplinary process should ensure correct and fair treatment for employees who are suspected of committing breaches of security. The formal disciplinary process should provide for a graduated response that takes into consideration factors such as the nature and gravity of the breach and its impact on business, whether or not this is a first or repeat offence, whether or not the violator was properly trained, relevant legislation, business contracts and other factors as required. In serious cases of misconduct the process should allow for instant removal of duties, access rights and privileges, and for immediate escorting out of the site, if necessary

| M4.4 | TERMINATION OR CHANGE OF EMPLOYMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that employees, contractors and third party users exit an <br> entity or change employment in an orderly manner |
| PERFORMANCE <br> INDICATOR | Percentage employees, contractors and third party user accounts that are <br> blocked after termination <br> Percentage of employees, contractors and third party users accounts <br> which profiles are modified based on role change |
| AUTOMATION <br> GUIDANCE | An identity management system could be used to automatically disable <br> terminated employee accounts and identify user accounts that are <br> inactive |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Abuse of system access/privileges <br> - Intentional leaks and sharing of data by staff <br> - Illegal processing of data |

--- Page 97 ---

| M4.4.1 | TERMINATION RESPONSIBILITIES | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall clearly define and assign responsibilities for performing employment termination or change of employment. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define an employee termination policy that emphasizes the communication of termination responsibilities in relation to entities information security (including confidentiality and property rights) <br> 2) Assign responsibility for performing termination or change of employment |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The communication of termination responsibilities should include ongoing security requirements and legal responsibilities and, where appropriate, responsibilities contained within any confidentiality agreement, and the terms and conditions of employment continuing for a defined period after the end of the employee's, contractor's or third party user's employment. |  |  |  |
| Responsibilities and duties still valid after termination of employment should be contained in employee's, contractor's or third party user's contracts. |  |  |  |
| Changes of responsibility or employment should be managed as the termination of the respective responsibility or employment, and the new responsibility or employment should be controlled. |  |  |  |


| M4.4.2 | RETURN OF <br> ASSETS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall ensure that all stakeholders should return all of <br> the entity's assets in their possession upon termination of their <br> employment, contract or agreement. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Include in employee termination policy that all employees, <br> contractors and third parties should return of all assets upon <br> termination of employment, contract or agreement |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

The termination process should be formalized to include the return of all previously issued software, corporate documents, and equipment. Other organizational assets such as mobile computing devices, credit cards, access cards, software, manuals, and information stored on electronic media also need to be returned.

In cases where an employee, contractor or third party user purchases the entity's equipment or uses their own personal equipment, procedures should be followed to ensure that all relevant information is transferred to the entity and securely erased from the equipment.

In cases where an employee, contractor or third party user has knowledge that is important to ongoing operations, that information should be documented and transferred to the entity.

--- Page 98 ---

| M4.4.3 | REMOVAL OF <br> ACCESS RIGHTS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |

CONTROL

The entity shall remove access rights of all stakeholders to information and information systems upon termination of their employment, contract or agreement, or adjusted upon change.
SUB-CONTROL

The entity shall:

1) Verify that the termination policy and procedure is followed for any termination or change of employment, contract or agreement with particular attention to revocation of credentials/access to any information facility

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Upon termination, the access rights of an individual to assets associated with information systems and services should be reconsidered. This will determine whether it is necessary to remove access rights. Changes of an employment should be reflected in removal of all access rights that were not approved for the new employment. The access rights that should be removed or adapted include physical and logical access, keys, identification cards, information systems, subscriptions, and removal from any documentation that identifies them as a current member of the entity. If a departing employee, contractor or third party user has known passwords for accounts remaining active, these should be changed upon termination or change of employment, contract or agreement.

Access rights for information assets and information systems should be reduced or removed before the employment terminates or changes, depending on the evaluation of risk factors such as:
A. Whether the termination or change is initiated by the employee, contractor or third party user, or by management and the reason of termination
B. The current responsibilities of the employee, contractor or any other user
C. The value of the assets currently accessible

--- Page 99 ---

# M5 COMPLIANCE 

| M5 | COMPLIANCE |
| :-- | :-- |
| OBJECTIVE | To ensure an entity is meeting all applicable requirements for <br> information security |
| PERFORMANCE <br> INDICATOR | Percentage of audit findings that are repeated |


| M5.1 | COMPLIANCE POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain a compliance policy, which is outlining the legal, technical, and <br> management security requirements that the entity needs to adhere to |
| PERFORMANCE <br> INDICATOR | Extent of compliance policy deployment and adoption across the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable compliance policy <br> - Unawareness of compliance policy among staff |


| M5.1.1 | COMPLIANCE <br> POLICY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall develop and maintain a compliance policy with which the entity must be compliant at the entity, sector, and national levels. |  |  |
| SUB-CONTROL | The compliance policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Outline the roles and responsibilities for establishing compliance requirements <br> 3) Outline the approach for establishing compliance requirements <br> 4) Outline the approach the entity will follow to ensure compliance with the identified requirements at the entity, sector, and national levels |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The compliance policy facilitates the implementation of the associated controls to ensure the entity is compliant at the entity, sector, and national levels. The policy includes applicable requirements, such as: <br> A. Information security legal requirements <br> B. Technical requirements <br> C. Non-technical requirements <br> In addition, the compliance policy typically outlines the considerations for information systems audit. The compliance policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |

--- Page 100 ---

| M5.2 | COMPLIANCE WITH INFORMATION SECURITY LEGAL REQUIREMENTS |
| :--: | :--: |
| OBJECTIVE | To avoid breaches of any information security legal, statutory, regulatory or contractual obligations |
| PERFORMANCE INDICATOR | Amount of time and resources spent by the legal department managing legal compliance issues with relation to information security |
| AUTOMATION GUIDANCE | Compliance automation tools are available for entities of all sizes and complexity. Selection of the appropriate compliance automation tool requires an entity to understand its regulatory environment, the risks it faces, and the maturity levels of its own compliance staff. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Breaches of legal requirements <br> - Unawareness of legal requirements <br> - Inaccurate identification of legal requirements |


| M5.2.1 | IDENTIFICATION OF APPLICABLE LEGISLATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall define, document and maintain all applicable legislation's (including statutory, regulatory, and contractual) compliance requirements with relation to information security and the entity's approach to meet these requirements. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop a process to identify on an ongoing basis all compliance requirements applicable to the entity <br> 2) Determine specific system requirements resulting from the identified compliance requirements <br> 3) Define specific controls to ensure all compliance requirements are met <br> 4) Periodically review compliance requirements and associated controls for completeness <br> 5) Document all legislation requirements with individual responsibilities to meet these requirements as well as controls in-place |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Applicable legislation for compliance consideration includes, but is not limited to, applicable federal laws, directives, regulations, policies, standards, and other guidance. <br> The specific controls and individual responsibilities to meet these requirements should be similarly defined and documented. |  |  |  |

--- Page 101 ---

| M5.2.2 | INTELLECTUAL <br> PROPERTY RIGHTS <br> (IPR) | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall implement the appropriate procedures to ensure compliance with legislative, regulatory, and contractual requirements on the use of material in respect of which there may be intellectual property rights and on the use of proprietary software products. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop and maintain an intellectual property rights compliance policy <br> 2) Develop a process to identify all applicable requirements the entity must meet in terms of protecting intellectual property rights <br> 3) Determine specific system requirements resulting from the identified requirements <br> 4) Define specific controls to ensure all intellectual property right protection requirements are met <br> 5) Periodically review requirements and associated controls for completeness |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The following guidelines should be considered to protect any material that may be considered intellectual property: <br> A. Publishing an intellectual property rights compliance policy which defines the legal use of software and information products <br> B. Acquiring software only through known and reputable sources, to ensure that copyright is not violated <br> C. Maintaining awareness of policies to protect intellectual property rights, and giving notice of the intent to take disciplinary action against personnel breaching them <br> D. Maintaining appropriate asset registers, and identifying all assets with requirements to protect intellectual property rights <br> E. Maintaining proof and evidence of ownership of licenses, master disks, manuals, etc. <br> F. Implementing controls to ensure that any maximum number of users permitted is not exceeded <br> G. Carrying out checks that only authorized software and licensed products are installed; <br> H. Providing a policy for maintaining appropriate license conditions <br> I. Providing a policy for disposing or transferring software to others <br> J. Using appropriate audit tools <br> K. Complying with terms and conditions for software and information obtained from public networks <br> L. Not duplicating, converting to another format or extracting from commercial recordings (film, audio- other than permitted by copyright law <br> M. Not copying in full or in part, books, articles, reports or other documents, other than permitted by copyright law |  |  |  |  |

--- Page 102 ---

| M5.2.3 | PROTECTION OF ORGANIZATIONAL RECORDS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall protect important records from loss, destruction, and falsification, in accordance with statutory, regulatory, contractual, and business requirements. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a process for identifying records with specific compliance requirements regarding loss, destruction, falsification, or other applicable characteristics <br> 2) Determine specific system requirements resulting from the identified requirements <br> 3) Define specific controls to ensure all record protection requirements are met <br> 4) Periodically review requirements and associated controls for completeness |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Records should be categorized into record types, e.g. accounting records, database records, transaction logs, audit logs, and operational procedures, each with details of retention periods and type of storage media. Any related cryptographic keying material and programs associated with encrypted archives or digital signatures, should also be stored to enable decryption of the records for the length of time the records are retained. |  |  |  |
| Consideration should be given to the possibility of deterioration of media used for storage of records. Storage and handling procedures should be implemented in accordance with manufacturer's recommendations. For long term storage, the use of paper and microfiche should be considered. Where electronic storage media are chosen, procedures to ensure the ability to access data (both media and format readability) throughout the retention period should be included, to safeguard against loss due to future technology change. |  |  |  |
| Data storage systems should be chosen such that required data can be retrieved in an acceptable timeframe and format, depending on the requirements to be fulfilled. |  |  |  |
| The system of storage and handling should ensure clear identification of records and of their retention period as defined by national or regional legislation or regulations, if applicable. This system should permit appropriate destruction of records after that period if they are not needed by the entity. <br> To meet these record safeguarding objectives, the following steps should be taken within an entity: <br> A. Guidelines should be issued on the retention, storage, handling, and disposal of records and information <br> B. A retention schedule should be drawn up identifying records and the period of time for which they should be retained <br> C. An inventory of sources of key information should be maintained <br> D. Appropriate controls should be implemented to protect records and information from loss, destruction, and falsification |  |  |  |

--- Page 103 ---

| M5.2.4 | DATA PROTECTION AND PRIVACY OF PERSONAL INFORMATION | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall ensure data protection and privacy as required in relevant legislation, regulations, and, if applicable, contractual clauses. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a process for identifying data with specific compliance requirements regarding protection and privacy <br> 2) Determine specific system requirements resulting from the identified requirements <br> 3) Define specific controls to ensure all data protection and privacy requirements are met <br> 4) Periodically review requirements and associated controls for completeness |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| An organizational data protection and privacy policy should be developed and implemented. This policy should be communicated to all persons involved in the processing of personal information. |  |  |  |  |
| Compliance with this policy and all relevant data protection legislation and regulations requires appropriate management structure and control. Often this is best achieved by the appointment of a person responsible, such as a data protection officer, who should provide guidance to managers, users, and service providers on their individual responsibilities and the specific procedures that should be followed. Responsibility for handling personal information and ensuring awareness of the data protection principles should be dealt with in accordance with relevant legislation and regulations. Appropriate technical and organizational measures to protect personal information should be implemented |  |  |  |  |

--- Page 104 ---

|  M5.2.5 | PREVENTION OF MISUSE OF INFORMATION SYSTEMS | PRIORITY | P3  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT  |
|  CONTROL | The entity shall deter users from using information systems for unauthorized purposes. |  |   |
|  SUB-CONTROL | The entity shall:
1) Clearly communicate to all stakeholders what is considered to be authorized use of information systems
2) Develop the capability to monitor information systems for unauthorized use
3) Take corrective action to stop unauthorized use of information systems when detected |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  Management should approve the use of information systems. Any use of these facilities for non-business purposes without management approval, or for any unauthorized purposes, should be regarded as improper use of the information systems. If any unauthorized activity is identified by monitoring or other means, this activity should be brought to the attention of the individual manager concerned for consideration of appropriate disciplinary and/or legal action. |  |  |   |
|  Legal advice should be taken before implementing monitoring procedures. All users should be aware of the precise scope of their permitted access and of the monitoring in place to detect unauthorized use. This can be achieved by giving users written authorization, a copy of which should be signed by the user and securely retained by the entity. Employees of an entity, contractors, and third party users should be advised that no access will be permitted except that which is authorized. |  |  |   |
|  At log-on, a warning message should be presented to indicate that the information systems being entered are owned by the entity and that unauthorized access is not permitted. The user has to acknowledge and react appropriately to the message on the screen to continue with the log-on process. |  |  |   |

--- Page 105 ---

| M5.2.6 | REGULATION OF <br> CRYPTOGRAPHIC <br> CONTROLS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL

SUB-CONTROL

The entity shall use cryptographic controls in compliance with all relevant legislations, regulations, and agreements.
The entity shall:

1) Define a process for identifying applicable compliance requirements regarding use of cryptographic controls within the entity
2) Determine specific system requirements resulting from the identified requirements
3) Define specific controls to ensure all cryptographic control requirements are met
4) Periodically review requirements and associated controls for completeness

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

The following items should be considered for compliance with the relevant legislations, regulations, and agreements:
A. Restrictions on import and/or export of computer hardware and software for performing cryptographic functions
B. Restrictions on import and/or export of computer hardware and software which is designed to have cryptographic functions added to it
C. Restrictions on the usage of encryption
D. Mandatory or discretionary methods of access by the countries' authorities to information encrypted by hardware or software to provide confidentiality of content

Legal advice should be sought to ensure compliance with national laws and regulations. Before encrypted information or cryptographic controls are moved to another country, legal advice should also be taken.

--- Page 106 ---

| M5.2.7 | LIABILITY TO THE <br> INFORMATION <br> SHARING | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall ensure that liability issues and remediation are clarified, understood and approved by all members of an information sharing community, to address situations in which information is intentionally or unintentionally disclosed. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify any liability issues and remediation requirements regarding unauthorized disclosure of information in all information sharing communities in which the entity participates <br> 2) Define specific remediation procedures for each relevant information sharing community <br> 3) Communicate to the relevant information sharing community any issues identified regarding remediation procedures |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Remediation should include, at a minimum, notification of any unauthorized disclosure back to the originator, with sufficient detail to identify the information disclosed. <br> Where possible, notification should be provided back to the source, even if the information has been sanitized and does not reveal its origin. This could be achieved by the intermediary of a trusted third party. <br> Unauthorized disclosure consequences could affect directly the responsible parties and might involve eliminating or restricting access to some members for some period of time to re-establish community trust. |  |  |  |  |


| M5.3 | COMPLIANCE WITH NON-TECHNICAL REQUIREMENTS |
| :-- | :-- |
| OBJECTIVE | To ensure compliance with the entity's information security policies and <br> standards |
| PERFORMANCE <br> INDICATOR | Percentage of information security management sub-controls that have <br> been implemented |
| AUTOMATION <br> GUIDANCE | Compliance automation tools are available for entities of all sizes and <br> complexity. Selection of the appropriate compliance automation tool <br> requires an entity to understand its regulatory environment, the risks it <br> faces, and the maturity levels of its own compliance staff. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Non-compliance with management requirements <br> - Inaccurate identification of managerial requirements <br> - Unawareness of management requirements |

--- Page 107 ---

| M5.3.1 | COMPLIANCE WITH SECURITY POLICIES AND STANDARDS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity's managers shall ensure that all security procedures within their area of responsibility are carried out correctly to achieve compliance with security policies and standards. |  |  |  |
|  | Managers shall: <br> 1) Identify all security procedures that fall within their area of responsibility <br> 2) Develop the capability to monitor the execution of identified security procedures <br> 3) Take corrective action when issues regarding the execution of security procedures are identified |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Managers should regularly review the compliance of information processing within their area of responsibility with the appropriate security policies, standards, and any other security requirements. |  |  |  |  |
| If any non-compliance is found as a result of the review, managers should: <br> A. Determine the causes of the non-compliance <br> B. Evaluate the need for actions to ensure that non-compliance do not recur <br> C. Determine and implement appropriate corrective action <br> D. Review the corrective action taken |  |  |  |  |
| Results of reviews and corrective actions carried out by managers should be recorded and these records should be maintained. Managers should report the results to the persons carrying out the independent reviews, when the independent review takes place in the area of their responsibility |  |  |  |  |


| M5.4 | COMPLIANCE WITH TECHNICAL REQUIREMENTS |
| :-- | :-- |
| OBJECTIVE | To ensure compliance of systems with technical security requirements |
| PERFORMANCE <br> INDICATOR | Percentage of information security technical sub-controls that have been <br> implemented |
| AUTOMATION <br> GUIDANCE | Compliance automation tools are available for entities of all sizes and <br> complexity. Selection of the appropriate compliance automation tool <br> requires an entity to understand its regulatory environment, the risks it <br> faces, and the maturity levels of its own compliance staff. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Non-compliance with technical requirements <br> - Inaccurate identification of technical requirements <br> - Unawareness of technical requirements |

--- Page 108 ---

| M5.4.1 | TECHNICAL COMPLIANCE CHECKING | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall ensure that information systems are regularly checked for compliance with the UAE IA Standards. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define and execute a process for routinely checking for technical compliance with security standards <br> 2) Ensure results of compliance checking is performed by, and the results are reviewed by, authorized personnel with adequate technical capabilities <br> 3) Report any issues detected during technical compliance checking to the appropriate authority for remediation |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. <br> Technical compliance checking should be performed either manually (supported by appropriate software tools, if necessary) by an experienced system engineer, and/or with the assistance of automated tools, which generate a technical report for subsequent interpretation by a technical specialist. <br> If penetration tests or vulnerability assessments are used, caution should be exercised as such activities could lead to a compromise of the security of the system. Such tests should be planned, documented and repeatable. <br> Any technical compliance check should only be carried out by competent, authorized persons, or under the supervision of such persons. |  |  |  |


| M5.5 | INFORMATION SYSTEMS AUDIT CONSIDERATIONS |
| :-- | :-- |
| OBJECTIVE | To maximize the effectiveness of the information systems audit process <br> taking into account NESA guidance in this regard |
| PERFORMANCE <br> INDICATOR | Percentage of audits interrupted due to operational or security issues |
| AUTOMATION <br> GUIDANCE | Compliance automation tools are available for entities of all sizes and <br> complexity. Selection of the appropriate compliance automation tool <br> requires an entity to understand its regulatory environment, the risks it <br> faces, and the maturity levels of its own compliance staff. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Wrongly performed internal audit <br> - Incorrect audit outcomes |

--- Page 109 ---

| M5.5.1 | INFORMATION <br> SYSTEMS AUDIT CONTROLS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL |  | The entity shall ensure that audit requirements and activities involving checks on operational systems are carefully planned and agreed to minimize the risk of disruptions to business processes. |  |  |
| SUB-CONTROL |  | The entity shall: <br> 1) assign responsibilities for internal audits of information system controls to an appropriate authority <br> 2) define audit requirements for information system controls <br> 3) outline an audit plan to meet audit requirements for information system controls <br> 4) highlight measures taken to ensure audit activities minimize the risk of disruptions to business processes |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |  |
| The following guidelines should be observed: <br> A. Audit requirements should be agreed with appropriate management <br> B. The scope of the checks should be agreed and controlled <br> C. The checks should be limited to read-only access to software and data <br> D. Access other than read-only should only be allowed for isolated copies of system files, which should be erased when the audit is completed, or given appropriate protection if there is an obligation to keep such files under audit documentation requirements <br> E. Resources for performing the checks should be explicitly identified and made available <br> F. Requirements for special or additional processing should be identified and agreed <br> G. All access should be monitored and logged to produce a reference trail; the use of timestamped reference trails should be considered for critical data or systems <br> H. All procedures, requirements, and responsibilities should be documented <br> I. The person(s) carrying out the audit should be independent of the activities audited |  |  |  |  |

--- Page 110 ---

|  M5.5.2 | PROTECTION OF
INFORMATION
SYSTEMS AUDIT
TOOLS | PRIORITY |  | P4  |
| --- | --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT |   |
|  CONTROL | The entity shall protect access to information systems audit tools to prevent any possible misuse or compromise. |  |  |   |
|  SUB-CONTROL | The entity shall:
1) Identify all information systems audit tools
2) Identify the types and classification levels of information stored in information systems audit tools
3) Define minimum security requirements for information systems audit tools commensurate to the classification levels of the information held |  |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |   |
|  Information systems audit tools, e.g. software or data files, should be separated from development and operational systems and not held in tape libraries or user areas, unless given an appropriate level of additional protection. |  |  |  |   |

|  M5.5.3 | AUDIT OF
COMMUNITY
FUNCTIONS | PRIORITY |  | P4  |
| --- | --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT |   |
|  CONTROL | The entity shall specify the audit rights of members to the information sharing community to which it is connected to. |  |  |   |
|  SUB-CONTROL | The entity shall:
1) Identify the audit rights of any information sharing communities to which it is connected
2) Ensure that provisions for external members are accounted for in the entity's information systems audit plan and tools
3) Ensure that provisions for the entity to exercise its audit rights are accounted for in the entity's information systems audit plan and tools |  |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |   |
|  The authority to audit entity's systems could be limited to a trusted third party taking into account NESA guidance in this regard. |  |  |  |   |

--- Page 111 ---

# M6 PERFORMANCE EVALUATION AND IMPROVEMENT 

| M6 | PERFORMANCE EVALUATION AND IMPROVEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that information security performance is measured, analyzed, <br> evaluated and improved, where necessary. |
| PERFORMANCE <br> INDICATOR | Compliance level achieved against the entity's information security <br> policy and objectives (e.g. by using the performance indicators <br> suggested in this Standard or the entity's own performance indicators to <br> produce a dashboard demonstrating compliance) |


| M6.1 | PERFORMANCE EVALUATION POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain a performance evaluation policy outlining the approach to <br> measure and evaluate the effectiveness of the information security of the <br> entity. |
| PERFORMANCE <br> INDICATOR | Percentage of successful performance measures applied |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - No performance evaluation <br> - Performance evaluation against wrong criteria |

--- Page 112 ---

| M6.1.1 | PERFORMANCE <br> EVALUATION <br> POLICY | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall have a policy for performance evaluation that sets the framework for all performance evaluations that take place in the entity. |  |  |  |
|  | The entity shall develop and implement a performance evaluation policy that determines: <br> 1) The overall framework for performance evaluation <br> 2) The methods of reporting the performance evaluation results to management <br> 3) How to integrate the detailed performance measurements for controls with higher level performance measurements for information security objectives, risk management, etc. <br> 4) How to integrate incident reports in the overall picture of performance monitoring |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Ongoing performance monitoring and evaluation is one of the major contributors to overall effective and success information security operation within any entity. Therefore, the entity should have an overall framework for its monitoring and performance measurement activities. These activities can have several sources of input: <br> A. High level performance evaluation activities, such as the performance indictors suggested for sub-families in this Standard <br> B. Detailed performance evaluation activities, such as the performance indictors suggested for "risk-based applicable" controls <br> C. Ongoing monitoring, which detects deviations and necessary corrections <br> D. Incident reports, which indicate that one or more of the controls are not working as intended |  |  |  |  |
| The performance evaluation policy should define how these different performance indicators are integrated within the entity to provide an overall picture of information security performance to management, and how the results of these performance measurement activities can be presented to management for decision-making. |  |  |  |  |


| M6.2 | PERFORMANCE EVALUATION |
| :-- | :-- |
| OBJECTIVE | To ensure that information security performance is measured, analyzed and <br> evaluated. |
| PERFORMANCE <br> INDICATOR | Percentage of all those con-conformities that have been detected and <br> not resolved within the time frame planned |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Non-compliance with controls of this Standard <br> - Under-performance of information security controls in place <br> - Ineffective controls |

--- Page 113 ---

| M6.2.1 | MONITORING, MEASUREMENT, ANALYSIS AND EVALUATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall monitor and evaluate the information security performance and the effectiveness of the information security management system. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Determine: <br> A. What needs to be monitored and measured, including information security processes and controls <br> B. The methods for monitoring, measurement, analysis and evaluation, as applicable, to ensure valid results <br> C. When the monitoring and measuring shall be performed <br> D. Who shall monitor and measure <br> E. When the results from monitoring and measurement shall be analyzed and evaluated <br> F. Who shall analyze and evaluate these results <br> 2) Document the monitoring and measurement methods and results. |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The continual improvement the entity needs to apply to its information security controls (see also M6.3.2) needs to make use of the monitoring and performance measurement results to identify which areas do require improvement. Therefore, these activities are key to keeping information security up to date, and fit for purpose of the entity's requirements. <br> The results of monitoring and review should be recorded and externally and internally reported as appropriate, and should also be used as an input to the review of the information security risk management policy (refer to M2.1.1). <br> The entity should develop a plan to execute the monitoring and performance measurement activities, including all of the topics mentioned in the sub-controls above. It can be helpful to have clear responsibilities and schedule to carry out the monitoring and measuring, and there should be an independent review function that ensures that this monitoring takes place. <br> In addition to executing the monitoring and measurement activities, there is also a need to keep these activities up to date and effective, so all monitoring and performance evaluation activities should be subject periodical reviews, as well as immediate updates if the situation requires that. <br> The results of the monitoring and performance evaluation activities should be put into context with respect to: <br> A. The information security policy (refer to M1.2.1) <br> B. The information security risk management policy (refer to M2.1.1) <br> C. Management expectations with regards to information security and the overall internal context (refer to M1.1.1) <br> D. external requirements for information security, e.g. by the sector, regional or national <br> The methods selected for the monitoring and performance measurement should produce consistent and comparable results to assist the entity in measuring performance over time. |  |  |  |

--- Page 114 ---

| M6.2.2 | INTERNAL AUDITS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall plan and conduct internal audits of the information security in place. |  |  |
|  | The entity shall: <br> 1) Define the audit criteria, scope and audit plan for each audit <br> 2) Select auditors and conduct audits to ensure objectivity and the impartiality of the audit process <br> 3) Ensure that the results of the audits are reported to relevant management <br> 4) Document the audit program and the audit results <br> 5) Ensure that the internal audit is effectively implemented and maintained |  |  |
| SUB-CONTROL | The internal audits shall: <br> 6) Be planned, established, implemented and maintained, including the frequency, methods, responsibilities, planning requirements, and reporting of the internal audits <br> 7) Take account of the importance of the processes concerned and the results of previous audits <br> 8) Ensure that entity's information security conforms to: <br> A. The entity's own requirements for information security <br> B. The requirements of this Standard <br> C. Any applicable requirements from the entity's sector, national or regulatory environment |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |
| Internal audits are another important means, in addition to the performance measurements, to assess compliance with the "always applicable" controls of this Standard, the entity's own policies and procedures, and the applicable requirements from the entity's sector, national or regulatory environment. |  |  |  |
| The information security controls in place at the entity should be subject to independent internal audits at a pre-defined schedule. This type of auditing should not come as a surprise but should be planned in advance, and the auditor should provide an audit plan of the areas to be audited and people to be met, to ensure the audit does not disrupt the business processes more than necessary (see also the sub-controls above). |  |  |  |
| One of the important concepts of internal audits is the independence of the internal auditor(s) carrying out the audits. If the necessary independence or expertise cannot be found within the entity, external resources can provide this service. If the entity uses external resources, care should be taken to ensure that the external resource have enough knowledge of the entity to successfully conduct the audit. |  |  |  |
| Another important aspect of the internal audit is the entity's reaction to its results. The results of the internal audits should be considered by the Information Security Committee (refer to M1.1.2), and it should be ensured that all findings of the audit are corrected in a timely manner. |  |  |  |

--- Page 115 ---

| M6.3 | IMPROVEMENT |
| :-- | :-- |
| OBJECTIVE | To correct nonconformities with this Standard and to continually improve <br> the information security program in place |
| PERFORMANCE <br> INDICATOR | Number of all non-conformities that have been detected and not <br> resolved within the time frame planned |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | Non-compliance with the controls in this Standard <br> Repeated incidents and inappropriate action to information security <br> problems <br> No improvements to information security |


| M6.3.1 | CORRECTIVE ACTION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | ALWAYS APPLICABLE |
| CONTROL | The entity shall correct any nonconformity with these Standards.. |  |  |
| SUB-CONTROL | The entity shall react to the nonconformity when it occurs, and take action to control and correct it, and to deal with the consequences. The entity shall: <br> 1) Evaluate the need for action to eliminate the causes of nonconformities, in order that it does not recur or occur elsewhere, by: <br> A. Reviewing the nonconformity <br> B. Determining the causes of the nonconformity <br> C. Determining if similar nonconformities exist, or could potentially occur <br> 2) Implement the appropriate action needed to the effects of the encountered nonconformities <br> 3) Review the effectiveness of any corrective action taken <br> 4) Document the corrective actions taken against the nonconformities |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The entity should have a clear action plan that describes how identified non-conformities will be addressed. This can take place in the Information Security Committee (refer to M1.1.2) and should be initiated and controlled by the Information Security Manager. Determine whether corrective action is justified on the basis of evaluating the following considerations: <br> A. Whether it is a first or a repeat occurrence <br> B. Frequency and history of occurrences (repeated occurrences) <br> C. Seriousness of the impact <br> D. Root cause for the non-conformity for which the following activities have to be performed - <br> - Collect data <br> - Get expert advice <br> - Consult with vendors, partners and associates |  |  |  |
| The corrective action(s) identified should be implemented within an appropriate timeframe and prioritized based on the risk treatment plan (see M2); delays should be avoided to reduce the negative effects of non-conformities to the information security in place at the entity. It is also important to ensure that the implemented corrective actions achieve their intended objective and are effective. The review of the effectiveness of corrective actions can be done by the Information Security Committee, and the results should be documented. |  |  |  |

--- Page 116 ---

|  M6.3.2 | CONTINUAL
IMPROVEMENT | PRIORITY | P2  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | ALWAYS APPLICABLE  |
|  CONTROL | The entity shall continually improve the information security program in place. |  |   |
|  SUB-CONTROL | The entity shall:
1) Improve the suitability, adequacy and effectiveness of information security controls in place
2) Take account of the performance measurement results and incidents when identifying improvements. |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  Based on results of monitoring and reviews, decisions should be made on how the information security in place, the controls, processes, policies and procedures can be improved. These decisions should lead to improvements in the entity's management of information security and its risk management culture. |  |  |   |
|  Continual improvement of information security can be done through the entity's performance indicators and measurements, incident reports, training, reviews and audits (refer to M6.1) and the subsequent modification of the entity's processes, systems, resources, capability and skills. |  |  |   |
|  Continual improvement is a very powerful concept and can help the entity to ensure that its information security is up to date and suitable for its needs. |  |  |   |

--- Page 117 ---

# 5.4 

## TECHNICAL CONTROLS

## T1 ASSET MANAGEMENT

| T1 | ASSET MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure information classification and protection of <br> organizational assets |
| PERFORMANCE <br> INDICATOR | Percentage of information assets that are adequately classified <br> and protected |
| T1.1 | ASSET MANAGEMENT POLICY |
| OBJECTIVE | To maintain an asset management policy outlining the procedures <br> to identify, classify and handle information assets |
| PERFORMANCE <br> INDICATOR | Extent of asset management policy deployment and adoption <br> across the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT THREATS <br> AND VULNERABILITIES | - Use of unapproved hardware and / or devices <br> - Physical theft of assets <br> - Retrieval of recycled or discarded media |

![img-12.jpeg](img-12.jpeg)

--- Page 118 ---

| T1.1.1 | ASSET <br> MANAGEMENT <br> POLICY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall establish an asset management policy. |  |  |
| SUB-CONTROL | The asset management policy shall: <br> 1) Be appropriate to the complexity of the entity and to the assets managed by the entity <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline the roles and responsibilities <br> 4) Provide the framework for managing the entity's assets, including assignment of owners <br> 5) Provide the framework for managing Bring Your Own Device (BYOD) arrangements <br> 6) Be documented and communicated to all users <br> 7) Be read and acknowledged formally by all users <br> 8) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The asset management policy provides a structure for the management of IT assets (e.g. people, hardware, software, data, facilities) from procurement to disposal. The policy can, for example, contain in addition to the required sub-controls: <br> A. IT Assets classification scheme <br> B. Classified assets security requirements <br> C. Disciplinary procedure <br> The asset management policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |

--- Page 119 ---

| T1.2 | RESPONSIBILITY FOR ASSETS |
| :--: | :--: |
| OBJECTIVE | To achieve and maintain appropriate protection of the entity's information assets |
| PERFORMANCE INDICATOR | Percentage of employees who have authorized access to information systems only after signing an acknowledgment of that they have read and understood rules of behavior |
| AUTOMATION GUIDANCE | As a pre-requisite for any automation to be used, entities should identify assets and their owners, and then deciding and documenting which part of the entity and/or individuals are responsible for each component of a business process (including information, software, and hardware, IT, etc.). <br> The entity could use a tool to automate the following processes: <br> - Tracking of information asset inventory, <br> - Assignment of information assets ownership <br> - Defining the right use of information assets <br> Some entities maintain asset inventories using specific large-scale commercial products dedicated to the task, or they use free solutions to track and then sweep the network periodically for new assets connected to it. In particular, when entities acquire new systems, they record the owner and features of each new asset, including its network interface Media Access Control (MAC) address and location. This mapping of asset attributes and owner-to-MAC address can be stored in a free or commercial database management system. <br> The entity should determine which asset attributes, based on entity's needs, should be tracked. The following list of potential attributes could be considered: <br> - Asset name <br> - Asset type <br> - Asset tag <br> - IP address <br> - MAC address <br> - Serial number <br> - Location; etc. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Use of unapproved hardware and / or devices <br> - Use of counterfeit or copied software <br> - Destruction of Equipment or Media |

--- Page 120 ---

| T1.2.1 | INVENTORY OF <br> ASSETS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall maintain an inventory list of all its information assets. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify an inventory of information assets within the entity <br> 2) Maintain an up-to-date list of assets <br> 3) Ensure accuracy and consistency with other inventories |  |  |

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

An entity should identify assets relevant in the lifecycle of information and document their importance. The lifecycle of information should include creation, processing, storage, transmission, deletion, destruction, protection. Documentation should be done in dedicated or existing inventories as appropriate and includes asset data such as type of asset, location, backup information, related licenses, and its importance / criticality.

The asset inventory should be accurate, up to date, consistent, and aligned with other inventories such as inventories in Enterprise Asset Management and Enterprise Resource Planning (ERP).

Here is a list of inventory assets that might be considered including, but not limited to:

## HARDWARE - SERVER

- Laptops, workstations, storage, security devices (firewall, IDS / IPS, anti-spam, etc.)


## NETWORK

- Routers, gateways, switches, Wireless Access Points, network segments (e.g. cabling and equipment between two computers), Others (SAT, Laser)


## PEOPLE

- Chief Technology / Information Director
- Information Technology Manager
- Database Development \& Administration (manager, analyst, architect, administrator etc.)
- Programming / Software Engineering (manager, engineer, programmer, tester etc.) Back


## OFFICE APPLICATIONS

- Financial control, customer care, logistics, ERP, CRM, Email


## CLIENT FACING APPLICATIONS

- E-commerce, Internet Service Provisioning - Static, Public IP addresses, DNS services, Registration and management, Email service provisioning, and Web portals


## DATA AND INFORMATION

- Customer personal data, customer financial data, entity's employee personal and financial data


## FACILITIES

- Headquarters, secondary premises, branch offices, offices, and data centers

--- Page 121 ---

| T1.2.2 | OWNERSHIP OF ASSETS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall assign a designated owner for each asset in the inventory. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish the process for the assignment of asset ownership and its periodical review <br> 2) Assign an owner with management responsibility for each identified asset |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The asset owner should be responsible for: <br> A. Ensuring that information and assets associated with information systems are appropriately classified <br> B. Defining and periodically reviewing access restrictions and classifications, taking into account applicable access control policies |  |  |  |
| Ownership may be allocated to: <br> - A business process <br> - A defined set of activities <br> - An application <br> - A defined set of data |  |  |  |


| T1.2.3 | ACCEPTABLE USE <br> OF ASSETS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall develop rules for the acceptable use of its information assets.. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish and document the rules for the acceptable use of assets <br> 2) Adapt rules to the different roles (management, users, <br> administrators, operators, contractors, etc.) <br> 3) Ensure circulation and acceptance of the rules by employees, <br> contractors and third parties <br> 4) ensure compliance with the established rules |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| All employees, contractors and third party users should follow rules for the acceptable use of information and assets associated with information systems, including: <br> A. Rules for electronic mail and Internet usages; <br> B. Guidelines for the use of mobile devices, especially for the use outside the premises of the entity |  |  |  |
| Specific rules or guidance should be provided by the relevant management. Employees, contractors and third party users using or having access to the entity's assets should be aware of the limits existing for their use of entity's information and assets associated with information systems, and resources. They should be responsible for their use of any information processing resources, and of any such use carried out under their responsibility. |  |  |  |
| Information provided by other members of an information sharing community is an asset, and should be protected and disseminated in accordance with any rules set by the information sharing community or by the originator. |  |  |  |

--- Page 122 ---

| T1.2.4 | ACCEPTABLE BRING YOUR OWN DEVICE (BYOD) ARRANGEMENTS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall develop rules for the acceptable use of information assets associated with BYOD arrangements. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish the rules for the acceptable use of personal assets that are used on the entity's environment <br> 2) Adapt rules to the different roles (management, users, administrators, operators, contractors, etc.) <br> 3) Ensure circulation and acceptance of the rules by employees, contractors and third parties <br> 4) Measure compliance with these rules |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| All employees, contractors and third party users should follow rules for the acceptable use of information and assets associated with BYOD arrangements, including: <br> A. Rules for phone, electronic mail and Internet usages <br> B. Rules for protection of the device from unauthorized access (e.g. pin code) <br> C. Rules for storing and / or encrypting personal and entity information <br> D. Clear separation of personal data and entity's data |  |  |  |
| It is recommended to ensure a complete split of personal and entity information by technical means. |  |  |  |


| T1.3 | INFORMATION CLASSIFICATION |
| :-- | :-- |
| OBJECTIVE | To ensure that information receives an appropriate level of protection |
| PERFORMANCE <br> INDICATOR | Percentage of information assets that are classification based on it <br> sensitivity, versus those that are not |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Tempering with sensitive information with no appropriate protection <br> - Unauthorized access to sensitive information |

--- Page 123 ---

| T1.3.1 | CLASSIFICATION OF INFORMATION | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall develop a classification scheme for its information. |  |  |
| SUB-CONTROL | The classification shall include: <br> 1) An information classification scheme based on information value, legal requirements, sensitivity, and criticality to the entity <br> 2) The degree of protection required for each category <br> The information classification scheme shall ensure: <br> 3) Information classification based on the established levels and mapped to accountable owners <br> 4) An up-to-date information classification in accordance with changes of their value, sensitivity and criticality through their life-cycle <br> 5) The possibility to be accessed by automated systems to enforce specific protections based on the classification level <br> 6) Sufficient information regarding physical assets (locations, data centers, networks, systems, storage, etc.) used to store, process or transmit information assets is provided |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |
| Classifications and associated protective controls for information should take account of business needs for sharing or restricting information, as well as legal requirements. Assets other than information can also be classified in conformance with classification of information which is stored in, processed by or otherwise handled or protected by the asset. |  |  |  |
| Classification scheme should include conventions for classification and criteria for review of the classification over time; in accordance with some predetermined access control policy. The level of protection in the scheme should be assessed by analyzing confidentiality, integrity and availability and any other requirements for the information considered. |  |  |  |
| Owners of information assets should be accountable for their classification. The scheme should be consistent across the whole entity so that everyone will classify information and related assets in the same way, have a common understanding of protection requirements and apply the appropriate protection. Each level should be given a name that makes sense in the context of the classification scheme's application. Classification should be included in the entity's processes, and consistent and coherent across the entity. Results of classification should indicate value of assets depending on their sensitivity and criticality to the entity, e.g. in terms of confidentiality, integrity and availability. Results of classification should be updated in accordance with changes of their value, sensitivity and criticality through their life-cycle. |  |  |  |

--- Page 124 ---

Classification provides people who deal with information a concise indication of how to handle and protect it. Creating groups of information with similar protection needs and specifying information security procedures that apply to all the information in the group facilitate this. This approach reduces the need for case-by-case risk assessment and custom design of controls.

An example of information confidentiality classification scheme could be based on four levels as follows:
A) Disclosure causes no harm
B) Disclosure causes minor embarrassment or minor operational inconvenience
C) Disclosure has a significant short term impact on operations or tactical objectives
D) Disclosure has a serious impact on long term strategic objectives or put the survival of the organization at risk

| T1.3.2 | LABELING OF <br> INFORMATION | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall label information in accordance with the classification scheme adopted by the entity. |  |  |  |
|  | The entity shall: <br> 1) Establish a procedure for labeling of information and its related assets in physical or electronic formats to reflect their attributed classification <br> 2) Apply the appropriate label on information |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Procedures for information labeling need to cover information and its related assets in physical and electronic formats. The labeling should reflect the classification scheme established in. The labels should be easily recognizable. The procedures should give guidance where and how labels are attached in consideration of how the information is accessed or the assets are handled depending on the types of media. The procedures can define cases where labeling is omitted, e.g. labeling of non-confidential information to reduce workloads. Employees and external party users should be made aware of labeling procedures. |  |  |  |  |
| Output from systems containing information that is classified as being sensitive or critical should carry an appropriate classification label in the output. |  |  |  |  |

--- Page 125 ---

| T1.3.3 | HANDLING OF <br> INFORMATION <br> ASSETS | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall handle assets in accordance with the information classification scheme adopted by the entity.

SUB-CONTROL
The entity shall:

1) Develop handling procedures for processing, storing and communicating information consistent with its classification and its attached label
2) Safeguard the information in accordance with the established procedures

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard.

Procedures should be drawn up for handling, processing, storing and communicating information consistent with its classification. The following items should be considered.
A. Handling of all media to its indicated classification level of the information stored on it
B. Access restrictions to prevent access from unauthorized personnel
C. Maintenance of a formal record of the authorized recipients of assets
D. Protection of temporary or permanent copies of information to a level consistent with the protection of the original information; storage of IT assets in accordance with manufacturers' specifications
E. Keeping the distribution of assets to a minimum required to support the entity's needs
F. Clear marking of all copies of media for the attention of the authorized recipient

The classification scheme used within the entity may not be equivalent to the schemes used by other entities, even if the names for levels are similar; in addition, information moving between entities may vary in classification depending on its context in each entity, even if their classification schemes are identical.

Agreements with other entities that include information sharing should include procedures to identify the classification of that information and to interpret the classification labels from other entities.

--- Page 126 ---

| T1.4 | MEDIA HANDLING |
| :-- | :-- |
| OBJECTIVE | To prevent unauthorized disclosure, modification, removal or destruction of <br> assets, and interruption to business activities |
| PERFORMANCE <br> INDICATOR | Percentage of physical backup/archive media that are fully encrypted |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Destruction of equipment or media <br> - Exploitation of backdoor or command and control channels <br> - Retrieval of recycled or discarded media |


| T1.4.1 | MANAGEMENT OF REMOVABLE MEDIA | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall manage the removable media in accordance with the classification scheme adopted by the entity. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish media management procedures along its lifecycle (setup, distribution, utilization and disposal) <br> 2) Identify the needed protection levels in accordance with the classification scheme <br> 3) Inhibit the use of removable media in those information systems that do not require it <br> 4) Control users of removable media |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Removable media such as optical discs (Blu-ray discs, DVDs, CDs), memory cards (CompactFlash card, Secure Digital card, Memory Stick), floppy disks / zip disks, disk packs, and magnetic tapes, are typically found in scanners, copiers, printers, notebook computers, workstations, network components, and mobile devices. |  |  |  |
| The following guidelines for the management of removable media should be considered: <br> A. If no longer required, the contents of any re-usable media that are to be removed from the entity should be made unrecoverable; data wiping software could be used for instance <br> B. Where necessary and practical, authorization should be required for media removed from the entity and a record of such removals should be kept in order to maintain an audit trail <br> C. All media should be stored in a safe, secure environment, in accordance with manufacturers' specifications <br> D. If data confidentiality or integrity are important considerations, cryptographic techniques should be used to protect data on removable media |  |  |  |

--- Page 127 ---

E. To mitigate the risk of media degrading while stored data are still needed, the data should be transferred to fresh media before it gets unreadable
F. Multiple copies of valuable data should be stored on separate media to further reduce the risk of coincident data damage or loss
G. Registration of removable media should be considered to limit the opportunity for data loss;
H. Prevent content auto-run on laptops, workstations, and servers for removable media
I. Removable media drives should only be enabled if there is a business reason for doing so

All procedures and authorization levels should be documented.

| T1.4.2 | DISPOSAL OF <br> MEDIA | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall dispose media when no longer needed.
SUB-CONTROL
The entity shall:

1) Establish procedures for secure disposal of media containing confidential information based on the sensitivity of that information
2) Destroy media, both paper and digital, when no longer serving the entity
3) Keep records for disposed media (containing or used to contain confidential information) when no longer needed

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Formal procedures for the secure disposal of media should be established to minimize the risk of confidential information leakage to unauthorized persons. The procedures for secure disposal of media containing confidential information should be corresponding with the sensitivity of that information.

The following items should be considered:
A. Media containing confidential information should be stored and disposed of securely and safely, e.g. by incineration or shredding, or erased of data for use by another application within the entity
B. Procedures should be in place to identify the items that might require secure disposal
C. It may be easier to arrange for all media items to be collected and disposed of securely, rather than attempting to separate out the sensitive items
D. Many entities offer collection and disposal services for media; care should be taken in selecting a suitable external party with adequate controls and experience
E. Disposal of sensitive items should be logged where possible in order to maintain an audit trail

When accumulating media for disposal, consideration should be given to the aggregation effect, which may cause a large quantity of non-confidential information to become sensitive.

--- Page 128 ---

# T2 PHYSICAL AND ENVIRONMENTAL SECURITY 

| T2 | PHYSICAL AND ENVIRONMENTAL SECURITY |
| :-- | :-- |
| OBJECTIVE | To prevent unauthorized physical access to the entity's facilities and <br> ensure security of information and equipment |
| PERFORMANCE <br> INDICATOR | Frequency of information security breaches related to physical and <br> environmental security |


| T2.1 | PHYSICAL AND ENVIRONMENTAL SECURITY POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain a physical and environmental security policy to outline the <br> security requirements of physical areas and equipment |
| PERFORMANCE <br> INDICATOR | Extent of physical and environmental security policy deployment and <br> adoption across the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable environmental security policy <br> - Unawareness of environmental security policy among staff <br> - Wrong classification of secure areas |


| T2.1.1 | PHYSICAL AND ENVIRONMENTAL SECURITY POLICY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall develop and maintain a physical and environmental security policy to ensure appropriate physical protection of assets. |  |  |  |
| SUB-CONTROL | The physical and environmental security policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline the roles and responsibilities for the physical and environmental security <br> 4) Consider the Information Assets classification and their physical location (storage, processing, transfer) <br> 5) Be documented and communicated to all users <br> 6) Be read and acknowledged formally by all users <br> 7) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |  |

--- Page 129 ---

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

The entity should develop, document, and disseminate the following documents to defined personnel or roles:
A. A physical and environmental security policy that addresses the purpose, scope, roles, responsibilities, management commitment, coordination to achieve appropriate physical protection among organizational entities, and compliance
B. Procedures to facilitate the implementation of the physical and environmental security policy and associated physical and environmental protection controls

The entity should ensure that the physical and environmental security policy and all supporting procedures are periodically reviewed and updated.

| T2.2 | SECURE AREAS |
| :-- | :-- |
| OBJECTIVE | To prevent unauthorized physical access, damage, and interference to <br> the entity's premises and information |
| PERFORMANCE <br> INDICATOR | Percentage of resolved / closed corrective items identified from periodic <br> physical security site surveys |
| AUTOMATION <br> GUIDANCE | Automated physical access management applications are available for <br> entities of all sizes and complexity and are deployed along physical access <br> control equipment (such as automated gates and doors). Selection of the <br> appropriate access management application requires an entity to have an <br> understanding of its physical landscape and locations, the risks it faces, and <br> the protection level required. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | Under protected secure areas <br> - Unauthorized access to secure areas <br> - Destruction of equipment of media <br> - Interference with security controls |

--- Page 130 ---

| T2.2.1 | PHYSICAL SECURITY PERIMETER | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall use security perimeters (barriers such as walls, card controlled entry gates or manned reception desks) to protect areas that contain information and information systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify and classify security areas based on the assets and information they process or contain <br> 2) Define security perimeters for every classified security level to ensure the right level of protection is applied <br> 3) Ensure the right security countermeasures are adopted to protect areas that contain information and information systems |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered and implemented where appropriate for physical security perimeters: <br> A. Security perimeters should be clearly defined, and the siting and strength of each of the perimeters should depend on the security requirements of the assets within the perimeter and the results of a risk assessment <br> B. Perimeters of a building or site containing information systems should be physically sound (i.e. there should be no gaps in the perimeter or areas where a break-in could easily occur); the external walls of the site should be of solid construction and all external doors should be suitably protected against unauthorized access with control mechanisms, e.g. bars, alarms, locks etc.; doors and windows should be locked when unattended and external protection should be considered for windows, particularly at ground level <br> C. A manned reception area or other means to control physical access to the site or building should be in place; access to sites and buildings should be restricted to authorized personnel only <br> D. Physical barriers should, where applicable, be built to prevent unauthorized physical access and environmental contamination <br> E. All fire doors on a security perimeter should be alarmed, monitored, and tested in conjunction with the walls to establish the required level of resistance in accordance to suitable regional, national, and international standards; they should operate in accordance with local fire code in a failsafe manner <br> F. Suitable intruder detection systems should be installed to national, regional or international standards and regularly tested to cover all external doors and accessible windows; unoccupied areas should be alarmed at all times; cover should also be provided for other areas, e.g. computer room or communications rooms <br> G. Information systems managed by the entity should be physically separated from those managed by third parties |  |  |

--- Page 131 ---

| T2.2.2 | PHYSICAL ENTRY CONTROLS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall protect secure areas by appropriate entry controls to ensure that only authorized personnel are allowed access. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Authenticate all persons accessing secure areas <br> 2) Document the access to secure areas <br> 3) Ensure that all persons wear some form of visible identification within the entity's premises <br> 4) Update and monitor access logs <br> 5) In case of contractors/third parties, they shall be always escorted, unless the area is explicitly designated for them with no escort requirement |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered: <br> A. The date and time of entry and departure of visitors should be recorded, and all visitors should be supervised unless their access has been previously approved; they should only be granted access for specific, authorized purposes and should be issued with instructions on the security requirements of the area and on emergency procedures <br> B. Access to areas where sensitive information is processed or stored should be controlled and restricted to authorized persons only; authentication controls, e.g. access control card plus PIN, should be used to authorize and validate all access; an audit trail of all access should be securely maintained <br> C. All employees, contractors and third party users and all visitors should be required to wear some form of visible identification and should immediately notify security personnel if they encounter unescorted visitors and anyone not wearing visible identification <br> D. Third party support service personnel should be granted restricted access to secure areas or sensitive information systems only when required; this access should be authorized and monitored <br> E. Access rights to secure areas should be regularly reviewed and updated, and revoked when necessary |  |  |  |

--- Page 132 ---

| T2.2.3 | SECURING <br> OFFICES, ROOMS <br> AND FACILITIES | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall design and apply physical security for offices, rooms, and facilities. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish rules to avoid access by the public to key facilities in line with the physical and environmental policy <br> 2) Avoid obvious signs that indicates the type of information or activities in the secure areas |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered to secure offices, rooms, and facilities: <br> A. Account should be taken of relevant health and safety regulations and standards <br> B. Key facilities should be sited to avoid access by the public <br> C. Where applicable, buildings should be unobtrusive and give minimum indication of their purpose, with no obvious signs, outside or inside the building identifying the presence of information processing activities <br> D. Directories and internal telephone books identifying locations of sensitive information systems should not be readily accessible by the public |  |  |  |


| T2.2.4 | PROTECTING <br> AGAINST <br> EXTERNAL AND <br> ENVIRONMENTAL <br> THREATS | PRIORITY | P4 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall design and apply physical protection against natural <br> disasters, malicious attack or accidents. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish policies and procedures for the storage of hazardous or <br> combustible materials to reduce their risks on secure areas in line <br> with the physical and environmental policy <br> 2) Secure fallback equipment and backup media from damage caused <br> by a natural or man-made disaster <br> 3) Ensure that all physical protection countermeasures and procedures <br> are aligned and coherent to Risk Assessment |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

Consideration should be given to any security threats presented by neighboring premises, e.g. a fire in a neighboring building, water leaking from the roof or in floors below ground level or an explosion in the street.

The following guidelines should be considered to avoid damage from fire, flood, earthquake, explosion, civil unrest, and other forms of natural or man-made disaster:
A. Hazardous or combustible materials should be stored at a safe distance from a secure area. Bulk supplies such as stationery should not be stored within a secure area;
B. Fallback equipment and backup media should be sited at a safe distance to avoid damage from a disaster affecting the main site;
C. Appropriate firefighting equipment should be provided and suitably placed.

--- Page 133 ---

| T2.2.5 | WORKING IN SECURE AREAS | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall design physical protection and guidelines for working in secure areas. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish guidelines for working in secure areas <br> 2) Make sure all personnel accessing secure areas is aware and accepts rules and guidelines <br> 3) Supervise activities in secure areas <br> 4) Control access of devices to secure areas (See also T5.7.1) |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered: <br> A. Personnel should only be aware of the existence of, or activities within, a secure area on a need to know basis <br> B. Unsupervised working in secure areas should be avoided both for safety reasons and to prevent opportunities for malicious activities <br> C. Vacant secure areas should be physically locked and periodically checked <br> D. Photographic, video, audio or other recording equipment, such as cameras in mobile devices, should not be allowed, unless authorized |  |  |  |
| The arrangements for working in secure areas include controls for the employees, contractors and third party users working in the secure area, as well as other third party activities taking place there |  |  |  |


| T2.2.6 | PUBLIC ACCESS, <br> DELIVERY, AND <br> LOADING AREAS | PRIORITY |  |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall control access points such as delivery and loading areas <br> and other points. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish access procedures to loading and unloading areas to <br> restrict access to only authorized personnel <br> 2) Physically segregate loading and unloading activities <br> 3) Inspect and register incoming and outgoing material in accordance <br> with the entity's asset management procedures |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered: <br> A. Access to a delivery and loading area from outside of the building should be restricted to <br> identified and authorized personnel <br> B. The delivery and loading area should be designed so that supplies can be unloaded without <br> delivery personnel gaining access to other parts of the building <br> C. The external doors of a delivery and loading area should be secured when the internal <br> doors are opened <br> D. Incoming material should be inspected for potential threats before this material is moved <br> from the delivery and loading area to the point of use <br> E. Incoming material should be registered in accordance with asset management procedures <br> on entry to the site <br> F. Incoming and outgoing shipments should be physically segregated, where possible |  |  |  |

--- Page 134 ---

| T2.3 | EQUIPMENT SECURITY |
| :-- | :-- |
| OBJECTIVE | To prevent loss, damage, theft or compromise of assets and interruption to <br> the entity's activities |
| PERFORMANCE <br> INDICATOR | Percentage of performed checks that revealed unauthorized movement <br> of information assets or other information security related issues |
| AUTOMATION <br> GUIDANCE | Solutions as physical access control, video surveillance and anti-intrusion <br> systems should be considered. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Equipment failure <br> - Tampering with equipment <br> - Physical theft of asset |


| T2.3.1 | EQUIPMENT SITING AND PROTECTION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall site and protect equipment. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish guidelines for the physical protection of equipment against unauthorized access <br> 2) Monitor the environmental conditions and alert in case of a potential threat |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered to protect equipment: <br> A. Equipment should be sited to minimize unnecessary access into work areas <br> B. Information systems handling sensitive data should be positioned carefully to reduce the risk of information being viewed by unauthorized persons during their use <br> C. Storage facilities should be secured to avoid unauthorized access <br> D. Items requiring special protection should be safeguarded to reduce the general level of protection required <br> E. Controls should be adopted to minimize the risk of potential physical and environmental threats, e.g. theft, fire, explosives, smoke, water (or water supply failure), dust, vibration, chemical effects, electrical supply interference, communications interference, electromagnetic radiation and vandalism <br> F. Guidelines for eating, drinking and smoking in proximity to information systems should be established <br> G. Environmental conditions, such as temperature and humidity, should be monitored for conditions, which could adversely affect the operation of information systems <br> H. Lightning protection should be applied to all buildings and lightning protection filters should be fitted to all incoming power and communications lines <br> I. The use of special protection methods, such as keyboard membranes, should be considered for equipment in industrial environments <br> J. Equipment processing confidential information should be protected to minimize the risk of information leakage due to electromagnetic emanation |  |  |

--- Page 135 ---

| T2.3.2 | SUPPORTING UTILITIES | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall protect equipment from disruptions caused by failures in supporting utilities. |  |  |  |
| SUB-CONTROL | Supporting utilities shall: <br> 1) Be tested for any malfunctioning <br> 2) Ensure protection and uninterrupted power supply on information systems <br> 3) Provide emergency lighting in case of main power failure <br> 4) Have up-to-date utilities maintenance logs |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Supporting utilities (e.g., electricity, telecommunications, water supply, natural gas, sewage, heating ventilation and air conditioning- should: <br> A. Conform to equipment manufacturer's specifications and local legal requirements <br> B. Be appraised regularly for their capacity to meet business growth and interactions with other supporting utilities <br> C. Be inspected and tested regularly to ensure their proper functioning <br> D. If necessary, be alarmed to detect malfunctions <br> E. If necessary, have multiple feeds with diverse physical routing |  |  |  |  |
| Emergency lighting and communications should be provided. Emergency switches and valves to cut off power, water, natural gas or other utilities should be located near emergency exits and/or equipment rooms. |  |  |  |  |

--- Page 136 ---

| T2.3.3 | CABLING SECURITY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall protect power and telecommunication cabling carrying data or supporting information services. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Protect power and telecommunication cables against physical tempering <br> 2) Segregated power and telecommunication cables to prevent interference <br> 3) Scan the network on a regular basis to identify unauthorized devices connected to the network (refer to T5.4.3) |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The following guidelines for cabling security should be considered: <br> A. Power and telecommunications lines into information systems should be underground, where possible, or subject to adequate alternative protection; <br> B. Power cables should be segregated from communications cables to prevent interference; <br> C. For sensitive or critical systems further controls to consider include: <br> 1) Installation of armored conduit and locked rooms or boxes at inspection and termination points; <br> 2) Use of electromagnetic shielding to protect the cables <br> 3) Initiation of technical sweeps and physical inspections for unauthorized devices being attached to the cables <br> 4) Controlled access to patch panels and cable rooms |  |  |  |  |

--- Page 137 ---

| T2.3.4 | EQUIPMENT <br> MAINTENANCE | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall maintain its equipment. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Document suppliers recommendations for the maintenance of equipment and make them available to maintenance personnel <br> 2) Establish policies and procedures for decommissioning and commissioning of equipment to ensure protection of sensitive data <br> 3) Keep a maintenance logs for all equipment |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines for equipment maintenance should be considered: <br> A. Equipment should be maintained in accordance with the supplier's recommended service intervals and specifications <br> B. Only authorized maintenance personnel should carry out repairs and service equipment; <br> C. Records should be kept of all suspected or actual faults, and of all preventive and corrective maintenance <br> D. Appropriate controls should be implemented when equipment is scheduled for maintenance, taking into account whether this maintenance is performed by personnel on site or external to the entity; where necessary, confidential information should be cleared from the equipment or the maintenance personnel should be sufficiently cleared <br> E. All maintenance requirements imposed by insurance policies should be complied with; <br> F. Before putting equipment back into operation after its maintenance ensure that the equipment has not been tampered with and/or does not malfunction |  |  |  |

--- Page 138 ---

| T2.3.5 | SECURITY OF EQUIPMENT OFF-PREMISES | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall apply security to off-site equipment. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish policies to protect off-site equipment in line with the physical and environmental policy (refer to M2.1.1) |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The use of any information storing and processing equipment outside the entity's premises should be authorized by management. This applies to equipment owned by the entity and those owned privately and used on behalf of the entity. <br> The following guidelines should be considered for the protection of off-site equipment: <br> A. Equipment and media taken off the premises should not be left unattended in public places; portable computers should be carried as hand luggage and disguised where possible when travelling <br> B. Manufacturers' instructions for protecting equipment should be observed at all times, e.g. protection against exposure to strong electromagnetic fields <br> C. Controls for off-premise locations, such as home-working, teleworking and temporary sites should be determined by a risk assessment and suitable controls applied as appropriate, e.g. lockable filing cabinets, clear desk policy, access controls for computers and secure communication with the office <br> D. It may be appropriate to avoid the risk by discouraging certain employees from working off-site and/or by restricting their use of portable IT equipment <br> E. When off-premises equipment is transferred among different individuals or external parties, a log should be maintained that defines the chain of custody for the equipment including at least names and entities of those who are responsible for the equipment <br> Risks, e.g. of damage, theft or eavesdropping, may vary considerably between locations and should be taken into account in determining the most appropriate controls. |  |  |

--- Page 139 ---

| T2.3.6 | SECURE DISPOSAL OR RE-USE OF EQUIPMENT | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall ensure that any sensitive data and licensed software has been removed or securely overwritten prior to disposal. |  |  |
| SUB-CONTROL | The entity shall: <br> A. Establish procedures for secure disposal or re-use of equipment based on the sensitivity of stored information <br> B. Keep record of disposed equipment when no longer needed |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Equipment should be verified to ensure whether storage media is contained or not prior to disposal or re-use. <br> Storage media containing confidential information should be physically destroyed or the information should be destroyed, deleted or overwritten using techniques to make the original information non-retrievable rather than using these Standards delete or format function. |  |  |  |


| T2.3.7 | REMOVAL OF <br> PROPERTY | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall authorize any equipment, information or software that <br> need to be taken off-site. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish an authorization procedure for taking information assets <br> off-site <br> 2) Maintain the list of information assets off-site with the authorized <br> employees, contractors and third party users |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered: <br> A. Equipment, information or software should not be taken off-site without prior authorization <br> B. Employees, contractors and third party users who have authority to permit off-site removal <br> of assets should be clearly identified <br> C. Time limits for equipment removal should be set and returns checked for compliance <br> D. Where necessary and appropriate, equipment should be recorded as being removed <br> off-site and recorded when returned |  |  |  |

--- Page 140 ---

| T2.3.8 | UNATTENDED <br> USER EQUIPMENT | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall ensure that unattended equipment has appropriate protection. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish user responsibilities and procedures when leaving equipment unattended <br> 2) Configure equipment and systems to implement automatic protections when left unattended |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| All users should be made aware of the security requirements and procedures for protecting unattended equipment, as well as their responsibilities for implementing such protection. Users should be advised to: <br> A. Terminate active sessions when finished, unless they can be secured by an appropriate locking mechanism, e.g. a password protected screen saver <br> B. Log-off from applications or network services when no longer needed <br> C. Secure computers or mobile devices from unauthorized use by a key lock or an equivalent control, e.g. password access, when not in use |  |  |  |


| T2.3.9 | CLEAR DESK AND <br> CLEAR SCREEN <br> POLICY | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall adopt a clear desk policy for papers and removable <br> storage media and a clear screen policy. |  |  |
| SUB-CONTROL | The clear desk and clear screen policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Outline the responsibilities of the users with respect to clear desk <br> and clear screen <br> 3) Be formalized and readily available to all users <br> 4) Be printed and made available to all desks subject to clear desk policy |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

The clear desk and clear screen policy should take into account the information classifications, legal and contractual requirements and the corresponding risks and cultural aspects of the entity. The following guidelines should be considered:
A. Sensitive or critical business information (e.g. on paper, flipcharts, white boards or on electronic storage media), should be locked away ideally in a safe or cabinet or other forms of security furniture when not required, especially when the office is vacated
B. Computers and terminals should be left logged off or protected with a screen and keyboard locking mechanism controlled by a password, token or similar user authentication mechanism when unattended and should be protected by key locks, passwords or other controls when not in use
C. Unauthorized use of photocopiers and other reproduction technology (e.g., scanners, digital cameras) should be prevented
D. Media containing sensitive or classified information should be removed from printers immediately

--- Page 141 ---

# T3 OPERATIONS MANAGEMENT 

| T3 | OPERATIONS MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure the effective operational control of the security functions <br> related to information and information systems |
| PERFORMANCE <br> INDICATOR | Frequency of operational failures leading to information security incidents |


| T3.1 | OPERATIONS MANAGEMENT POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain an operations management policy and to provide guidance <br> regarding the operational requirements of information assets |
| PERFORMANCE <br> INDICATOR | Extent of operations management security policy deployment and <br> adoption across the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | Unsuitable operations management policy <br> - Unawareness of operations management policy among staff |


| T3.1.1 | OPERATIONS <br> MANAGEMENT <br> POLICY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall establish an operations management policy. |  |  |  |
| SUB-CONTROL | The Operations Management Policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Provide the framework for managing the operations of systems, processes, and controls related to information security |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The operations management policy defines and documents operational standards and procedures across the IT lifecycle (planning, design, implementation, operations, and maintenance) necessary to maximize information security. The policy can, for example, contain: <br> A. Scope of the policy <br> B. Segregation of duties <br> C. Configuration management <br> D. Change request <br> E. Quality management <br> F. Backup procedures <br> G. Monitoring procedures |  |  |  |  |
| The operations management policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |  |

--- Page 142 ---

| T3.2 | OPERATIONAL PROCEDURES AND RESPONSIBILITIES |
| :-- | :-- |
| OBJECTIVE | To ensure the correct and secure operation of information systems |
| PERFORMANCE <br> INDICATOR | Percentage of information systems that meet all operational information <br> security requirements |
| AUTOMATION <br> GUIDANCE | Entities can implement control T3.2.1 by developing a series of images and <br> secure storage servers for hosting these standard images. Commercial and/ <br> or free configuration management tools can then be employed to measure <br> the settings operating system and applications of managed machines to look <br> for deviations from these Standards image configurations used by the entity. <br> Some configuration management tools require that an agent be installed <br> on each managed system, while others remotely log in to each managed <br> machine using administrator credentials. Either approach or a combination <br> of the two approaches can provide the information needed for this control. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Illegal processing of data <br> - Abuse of system access/privileges <br> - Equipment malfunction |


| T3.2.1 | COMMON <br> SYSTEMS <br> CONFIGURATION <br> GUIDELINES | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |
| CONTROL | The entity shall develop recommended configuration settings for <br> common information technology products. |  |  |
| SUB-CONTROL | The guidelines shall: <br> 1) Identify common information technology products used within <br> the entity <br> 2) Define minimum security configurations to be employed in <br> each product |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Configuration settings guidelines for common information technology products should <br> be created based on best practices and entity needs. These guidelines should be followed <br> where applicable within the information system. Such products include operating systems <br> (e.g., Microsoft Windows, Solaris) and databases (e.g., MS SQL, Oracle) and other products <br> commonly used within the entity. |  |  |  |

--- Page 143 ---

| T3.2.2 | DOCUMENTED <br> OPERATING <br> PROCEDURES | PRIORITY |  |
| :-- | :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall document operating procedures. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Document operating procedures in a format that facilitates <br> dissemination to all relevant stakeholders <br> 2) Ensure operating procedures are reviewed periodically <br> 3) Ensure all relevant stakeholders are aware of and have access to <br> relevant operating procedures |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Documented procedures should be prepared for system activities associated with information <br> processing and communication systems, such as computer start-up and close-down <br> procedures, back- up, equipment maintenance, media handling, computer room and mail <br> handling management, and safety. |  |  |  |
| The operating procedures should specify the instructions for the detailed execution of each <br> job including: |  |  |  |
| A. Processing and handling of information <br> B. Backup <br> C. Scheduling requirements, including interdependencies with other systems, earliest job <br> start and latest job completion times <br> D. Instructions for handling errors or other exceptional conditions, which might arise during <br> job execution, including restrictions on the use of system utilities <br> E. Support contacts in the event of unexpected operational or technical difficulties <br> F. Special output and media handling instructions, such as the use of special stationery or the <br> management of confidential output including procedures for secure disposal of output <br> from failed jobs <br> G. System restart and recovery procedures for use in the event of system failure <br> H. The management of audit-trail and system log information |  |  |  |
| Operating procedures, and the documented procedures for system activities, should be <br> treated as formal documents and changes authorized by management. Where technically <br> feasible, information systems should be managed consistently, using the same procedures, <br> tools, and utilities |  |  |  |

--- Page 144 ---

| T3.2.3 | CHANGE <br> MANAGEMENT | PRIORITY | P4 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY |  |
| CONTROL | The entity shall control the changes to information systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Document a change management process <br> 2) Integrate specific process controls to ensure the change management process is executed correctly <br> 3) Define the systems to which the change management process applies <br> 4) Assign management responsibilities for control of changes to identified systems |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Operational systems and application software should be subject to strict change management control. In particular, the following items should be considered: <br> A. Identification and recording of significant changes <br> B. Planning and testing of changes <br> C. Assessment of the potential impacts, including security impacts, of such changes <br> D. Formal approval procedure for proposed changes <br> E. Communication of change details to all relevant persons <br> F. Fallback procedures, including procedures and responsibilities for aborting and recovering from unsuccessful changes and unforeseen events |  |  |  |
| Formal management responsibilities and procedures should be in place to ensure satisfactory control of all changes to equipment, software or procedures. When changes are made, an audit log containing all relevant information should be retained. |  |  |  |


| T3.2.4 | SEGREGATION OF <br> DUTIES | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall segregate duties and areas of responsibility. |  |  |
| SUB-CONTROL | TThe entity shall: <br> 1) Identify specific sets of duties that should be segregated <br> 2) Ensure duties with segregation requirements are assigned to <br> different resources <br> 3) Implement suitable alternative controls in the case that duties with <br> segregation requirements cannot be assigned to different resources |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Segregation of duties is a method for reducing the risk of accidental or deliberate system <br> misuse. Care should be taken that no single person can access, modify or use assets without <br> authorization or detection. The initiation of an event should be separated from its authorization. <br> The possibility of collusion should be considered in designing the controls. |  |  |  |
| Small entities may find segregation of duties difficult to achieve, but the principle should be <br> applied as far as is possible and practicable. Whenever it is difficult to segregate, other controls <br> such as monitoring of activities, audit trails and management supervision should be considered. <br> It is important that security audit remains independent. |  |  |  |

--- Page 145 ---

| T3.2.5 | SEPARATION OF DEVELOPMENT, TEST AND OPERATIONAL FACILITIES | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall separate development, test, and operational environment. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the appropriate level of separation between operational, test, and development environments <br> 2) Define the rules for transferring software and systems from one environment to another <br> 3) Ensure the rules are integrated into the system / software development lifecycle |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The level of separation between operational, test, and development environments that is necessary to prevent operational problems should be identified and appropriate controls implemented. The following items should be considered: <br> A. Rules for the transfer of software from development to operational status should be defined and documented <br> B. Development and operational software should run on different systems or computer processors and in different domains or directories <br> C. Compilers, editors, and other development tools or system utilities should not be accessible from operational systems when not required <br> D. The test system environment should emulate the operational system environment as closely as possible <br> E. Users should use different user profiles for operational and test systems, and menus should display appropriate identification messages to reduce the risk of error <br> F. Sensitive data should not be copied into the test system environment |  |  |  |

--- Page 146 ---

| T3.3 | SYSTEM PLANNING AND ACCEPTANCE |
| :-- | :-- |
| OBJECTIVE | To ensure security requirements are properly considered during the <br> development lifecycle of information systems |
| PERFORMANCE <br> INDICATOR | Percentage of information systems that successfully integrated all <br> system development lifecycle security requirements |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Equipment failure <br> - Illegal processing of data <br> - Use of counterfeit or copied software |


| T3.3.1 | CAPACITY <br> MANAGEMENT | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall manage the required capacity. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Have the ability to measure capacity of current systems and estimate capacity requirements of planned systems <br> 2) Integrate capacity management controls into relevant demand management and software / system development lifecycle processes <br> 3) Make necessary adjustments to capacity to maintain required system performance |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| For each new and ongoing activity, capacity requirements should be identified. System tuning and monitoring should be applied to ensure and, where necessary, improve the availability and efficiency of systems. Detective controls should be put in place to indicate problems in due time. Projections of future capacity requirements should take account of new business and system requirements and current and projected trends in the entity's information processing capabilities. <br> Particular attention needs to be paid to any resources with long procurement lead times or high costs; therefore managers should monitor the utilization of key system resources. They should identify trends in usage, particularly in relation to business applications or management information system tools. <br> Managers should use this information to identify and avoid potential bottlenecks and dependence on key personnel that might present a threat to system security or services, and plan appropriate action. |  |  |  |  |

--- Page 147 ---

| T3.3.2 | SYSTEM <br> ACCEPTANCE AND TESTING | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall establish acceptance criteria for new information systems, upgrades, and new versions, in addition to suitable tests of the system(s) carried out during development and prior to acceptance. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define the requirements for testing new / updated systems prior to placing them in the operational environment <br> 2) Define the acceptable parameters for each requirement <br> 3) Ensure tests are carried out and that results are documented <br> 4) Formally assign responsibility for ensuring tests are completed prior to accepting new systems into operational environment |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. <br> Managers should ensure that the requirements and criteria for acceptance of new systems are clearly defined, agreed, documented, and tested. New information systems, upgrades, and new versions should only be migrated into production after obtaining formal acceptance. The following items should be considered prior to formal acceptance being provided: <br> A. Performance and computer capacity requirements <br> B. Error recovery and restart procedures, and contingency plans <br> C. Preparation and testing of routine operating procedures to defined standards; <br> D. Agreed set of security controls in place <br> E. Effective manual procedures <br> F. Business continuity arrangements <br> G. Evidence that installation of the new system will not adversely affect existing systems, particularly at peak processing times, such as month end <br> H. Evidence that consideration has been given to the effect the new system has on the overall security of the entity <br> I. Training in the operation or use of new systems <br> L. Ease of use, as this affects user performance and avoids human error <br> For major new developments, the operations function and users should be consulted at all stages in the development process to ensure the operational efficiency of the proposed system design. Appropriate tests should be carried out to confirm that all acceptance criteria have been fully satisfied. |  |  |  |  |

--- Page 148 ---

| T3.4 | PROTECTION FROM MALWARE- |
| :--: | :--: |
| OBJECTIVE | To ensure that information and information systems are protected against malware |
| PERFORMANCE INDICATOR | Percentage of information systems with appropriate and up-to-date protection as defined in information security requirements |
| AUTOMATION GUIDANCE | Relying on policy and user action to keep anti-malware tools up to date has been widely discredited, as many users have not proven capable of consistently handling this task. To ensure anti-virus signatures are up to date, entities use automation. They use the built-in administrative features of enterprise endpoint security suites to verify that anti-virus, anti-spyware, and host-based IDS features are active on every managed system. They run automated assessments daily and review the results to find and mitigate systems that have deactivated such protections, as well as systems that do not have the latest malware definitions. <br> Some entities deploy free or commercial honeypot and tarpit tools to identify attackers in their environment. Security personnel should continuously monitor honeypots and tarpits to determine whether traffic is directed to them and account logins are attempted. When they identify such events, these personnel should gather the source address from which this traffic originates and other details associated with the attack for follow-on investigation. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Spyware <br> - Backdoor or command and control <br> - SQL injection |


| T3.4.1 | CONTROLS <br> AGAINST <br> MALWARE | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall protect its information assets from malware. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Employ anti-malware protection mechanisms for the network as well <br> as servers, workstations, laptops and other devices connected to it <br> 2) Ensure that all anti-malware protection are up-to-date <br> 3) Periodically scan all information systems files as well as files <br> downloaded from public networks <br> 4) Scan all email attachments before reaching user's inbox <br> 5) Scan removable media for malware every time they are connected <br> to the information systems <br> 6) Configure servers, workstations, laptops so that they don't "auto- <br> run" contents from removable media <br> 7) Monitor anti-malware protection tools for malware detection <br> events that should be logged and a notification should be sent to the <br> administrators (refer to T.3.6.2) <br> 8) Ensure that users are aware of malware risks, behaviors and <br> preventative actions (refer to M.3.2.1) |  |  |

--- Page 149 ---

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Malware includes, for example, viruses, worms, Trojan horses, and spyware. Malware can also be encoded in various formats (e.g., UUENCODE, Unicode), contained within compressed or hidden files, or hidden in files using steganography.

Protection against malware should be based on malware detection and repair software, security awareness, and appropriate system access and change management controls. The following guidance should be considered:
A. Establishing a formal policy prohibiting the use of unauthorized software;
B. Establishing a formal policy to protect against risks associated with obtaining files and software either from or via external networks, or on any other medium, indicating what protective measures should be taken;
C. Conducting regular reviews of the software and data content of systems supporting critical business processes; the presence of any unapproved files or unauthorized amendments should be formally investigated;
D. Installation and regular update of software that detects and eradicate malware to scan computers and media as a precautionary control, or on a routine basis; the checks carried out should include:

- Reviewing any files received over networks or via any form of storage medium, for malware before use;
- reviewing electronic mail attachments and downloads for malware before use; this check should be carried out at different places, e.g. at electronic mail servers, desk top computers and when entering the network of the entity;
- Checking web pages for malware;
E. Defining management procedures and responsibilities to deal with malware protection on systems, training in their use, reporting and recovering from malware attacks;
F. Preparing appropriate business continuity plans (refer to T9.2.2) for recovering from malware attacks, including all necessary data and software backup and recovery arrangements;
G. Implementing procedures to regularly collect information, such as subscribing to mailing lists and/or checking web sites giving information about new malware;
H. Implementing procedures to verify information relating to malware, and ensure that warning bulletins are accurate and informative; managers should ensure that qualified sources, e.g. reputable journals, reliable Internet sites or suppliers producing software protecting against malware, are used to differentiate between hoaxes and real malware; all users should be made aware of the problem of hoaxes and what to do on receipt of them;
I. Isolate environments where catastrophic impacts may result.

Additional measures can include:

- Monitor workstations, servers, and mobile devices for active, up-to-date anti-malware protection with anti-virus, anti-spyware, personal firewalls, and host-based IPS functionality
- Prevent content auto-run on laptops, workstations, and servers
- Scan information systems periodically and files coming from external sources (including email attachments) in real-time
- Periodically update the protection mechanism

--- Page 150 ---

| T3.5 | BACKUP |
| :--: | :--: |
| OBJECTIVE | To maintain the integrity and availability of information and information systems |
| PERFORMANCE INDICATOR | Percentage of successful attempts to restore backup information, whether in test or real-world environments |
| AUTOMATION GUIDANCE | Commercial backup solutions are available to automatically perform information backup for designated systems. Entities deploying such solutions should carefully consider the following as examples: <br> - What information should be covered during backup <br> - When and at which frequency the backups should be conducted <br> - Where the backup data will be stored <br> - What is the required total size of the medium to store the backups. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Loss of information <br> - Software malfunction <br> - Destruction of equipment or media |

--- Page 151 ---

| T3.5.1 | INFORMATION <br> BACKUP | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall backup copies of its information and software.

SUB-CONTROL
The entity shall:

1) Establish guidelines for determining what information and software requires backup and how often
2) Establish and document clear backup procedures and system capabilities for all applicable backup requirements
3) Ensure backed up information and software is routinely tested for reliability
4) Ensure IT staff have the skills and qualification to conduct the backup procedures (refer to M1.4.1)

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
Adequate backup systems should be provided to ensure that all essential information and software can be recovered following a disaster or media failure.
The following items for information backup should be considered:
A. The necessary level of backup information should be defined;
B. Accurate and complete records of the backup copies and documented restoration procedures should be produced;
C. The extent (e.g. full or differential backup) and frequency of backups should reflect the business requirements of the entity, the security requirements of the information involved, and the criticality of the information to the continued operation of the entity;
D. Backups should be stored in a remote location, at a sufficient distance to escape any damage from a disaster at the main site;
E. Backup information should be given an appropriate level of physical and environmental protection consistent with these Standards applied at the main site; the controls applied to media at the main site should be extended to cover the backup site;
F. Backup media should be regularly tested to ensure that they can be relied upon for emergency use when necessary;
G. Restoration procedures should be regularly checked and tested to ensure that they are effective and that they can be completed within the time allotted in the operational procedures for recovery;
H. In situations where confidentiality is of importance, backups should be protected by means of encryption.

Backup arrangements for individual systems should be regularly tested to ensure that they meet the requirements of business continuity plans (refer to T9.2.2). For critical systems, the backup arrangements should cover all systems information, applications, and data necessary to recover the complete system in the event of a disaster.

The retention period for essential business information, and also any requirement for archive copies to be permanently retained should be determined.

Once per quarter (or whenever new backup equipment is purchased), a testing team should evaluate a random sample of system backups by attempting to restore them on a test bed environment. The restored systems should be verified to ensure that the operating system, application, and data from the backup are all intact and functional.

--- Page 152 ---

| T3.6 | MONITORING |
| :--: | :--: |
| OBJECTIVE | To detect, prevent and correct the use of systems and information based on audit logs of events that could impact the security of an entity. |
| PERFORMANCE INDICATOR | Percentage of incidents within the entity where sufficient and accurate information was available to detect and manage the incident |
| AUTOMATION GUIDANCE | Most free and commercial operating systems, network services, and firewall technologies offer logging capabilities. Such logging should be activated, with logs sent to centralized logging servers. Firewalls, proxies, and remote access systems (VPN, dial-up, etc.) should all be configured for verbose logging, storing all the information available for logging in the event a followup investigation is required. Furthermore, operating systems, especially those of servers, should be configured to create access control logs when a user attempts to access resources without the appropriate privileges. To evaluate whether such logging is in place, an entity should periodically scan through its logs and compare them with the asset inventory in order to ensure that each managed item actively connected to the network is periodically generating logs. <br> Analytical programs such as SIM/SEM solutions for reviewing logs can provide value, but the capabilities employed to analyze audit logs are quite extensive, including, importantly, even just a cursory examination by a person. Actual correlation tools can make audit logs far more useful for subsequent manual inspection. Such tools can be quite helpful in identifying subtle attacks. However, these tools are neither a panacea nor a replacement for skilled information security personnel and system administrators. Even with automated log analysis tools, human expertise and intuition are often required to identify and understand attacks. |
| RELEVANT THREATS AND VULNERABILITIES | - Unauthorized access <br> - Tempering with information systems <br> - Backdoor or command and control |

--- Page 153 ---

| T3.6.1 | MONITORING <br> POLICY AND PROCEDURES | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall establish a monitoring policy and related procedures. |  |  |
| SUB-CONTROL | The monitoring policy and related procedures shall: <br> 1) Outline what system aspects shall be monitored, how they shall be monitored, and how often they shall be monitored <br> 2) Assign responsibility for monitoring activities <br> 3) Define how information from monitoring activities will be fed into the incident response process <br> 4) Account for any sector or national requirements regarding information to be shared with external entities <br> 5) Be documented |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The entity should define events that need to be captured, the frequency of audit log reviews, and retention requirements for audit logs. Monitoring procedures should be developed, detailing the steps of the monitoring, the response actions and how the monitoring process feeds into the incident response process. Clear responsibilities should be assigned for the personnel performing monitoring. Each addition/change of systems in the facility should be considered for the amendment of the monitoring policy and procedures, to ensure they properly cover the updated environment. |  |  |  |

--- Page 154 ---

|  T3.6.2 | AUDIT LOGGING | PRIORITY | P2  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT  |
|  CONTROL | The entity shall produce and keep audit logs recording user activities, exceptions, and information security events. |  |   |
|  SUB-CONTROL | The entity shall:
1) Identify all activities to be captured in audit logs for all hardware devices, operating systems and installed applications
2) Identify minimum information requirements for each activity to be captured
3) Define minimum frequency requirements for reviewing audit logs
4) Ensure audit logs are reviewed by personnel with appropriate training and skills
5) Define minimum time requirements for maintaining audit logs |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  Entities should log local and remote access (including failed attempts) to and from all hardware devices, operating systems and installed applications, ensuring that logs include a date, timestamp, source addresses, destination addresses, and various other useful elements of each packet and/or transaction.
Audit logs should include, when relevant:
A. User IDs
B. Dates, times, and details of key events, e.g. log-on and log-off
C. Terminal identity or location if possible
D. Records of successful and rejected system access attempts
E. Records of successful and rejected data and other resource access attempts
F. Changes to system configuration
G. Use of privileges
H. Use of system utilities and applications
I. Files accessed and the kind of access
J. Network addresses and protocols
K. Alarms raised by the access control system
L. Activation and de-activation of protection systems, such as anti-virus systems and intrusion detection systems |  |  |   |

--- Page 155 ---

| T3.6.3 | MONITORING SYSTEM USE | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall monitor the use of information systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all types of system use to be monitored <br> 2) Identify minimum information gathering requirements for each monitoring activity <br> 3) Define minimum frequency requirements for reviewing information gathered from monitoring activities <br> 4) Ensure information gathered from monitoring activities is reviewed by personnel with appropriate training and skills <br> 5) Define minimum time requirements for maintaining information gathered from monitoring activities |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The level of monitoring required for individual systems should be determined by a risk assessment. An entity should comply with all relevant legal requirements applicable to its monitoring activities. Areas that should be considered include: <br> A. Authorized access, including detail such as: <br> 1- The user ID <br> 2- The date and time of key events <br> 3- The types of events <br> 4- The files accessed <br> 5- The program/utilities used <br> B. All privileged operations, such as <br> 1- Use of privileged accounts, e.g. supervisor, root, administrator <br> 2- System start-up and stop <br> 3- I/O device attachment/detachment <br> 4- Deleting, creating and granting privileges activities <br> C. Unauthorized access attempts, such as: <br> 1- Failed or rejected user actions <br> 2- Failed or rejected actions involving data and other resources <br> 3- Access policy violations and notifications for network gateways and firewalls <br> 4- Alerts from proprietary intrusion detection systems <br> D. System alerts or failures, such as: <br> 1- Console alerts or messages <br> 2- System log exceptions <br> 3- Network management alarms <br> 4- Alarms raised by the access control system <br> E. Database activities, such as: <br> 1- Use of privileged accounts <br> 2- Backup / restore <br> 3- Failed or rejected user actions <br> F. Changes to, or attempts to change, system security settings and controls. |  |  |
| How often the results of monitoring activities are reviewed should depend on the risks involved. Risk factors that should be considered include the: <br> A. Criticality of the application processes <br> B. Value, sensitivity, and criticality of the information involved <br> C. Past experience of system infiltration and misuse, and the frequency of vulnerabilities being exploited <br> D. Extent of system interconnection (particularly public networks) <br> E. Logging facility being de-activated |  |  |  |

--- Page 156 ---

| T3.6.4 | PROTECTION OF <br> LOG INFORMATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall protect log information against tampering and unauthorized access. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the log information across all information systems that shall be protected <br> 2) Ensure log information are protected commensurate to the sensitivity of the content of the logs |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Controls should aim to protect against unauthorized changes and operational problems with the logging facility including: <br> A. Alterations to the message types that are recorded; <br> B. Log files being edited or deleted; <br> C. Storage capacity of the log file media being exceeded, resulting in either the failure to record events or over-writing of past recorded events. <br> Some audit logs may be required to be archived as part of the record retention policy or because of requirements to collect and retain evidence. |  |  |  |


| T3.6.5 | ADMINISTRATOR <br> AND OPERATOR <br> LOGS | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall log system administrator and system operator activities.
The entity shall:

1) Identify all activities to be captured in administrator and operator logs
2) Identify minimum information requirement's for each activity to be captured
3) Define minimum frequency requirements for reviewing administrator and operator logs
4) Ensure administrator and operator logs are reviewed by personnel with appropriate training and skills
5) Define minimum time requirements for maintaining administrator and operator logs

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
Logs should include:
A. The time at which an event (success or failure- occurred;
B. Information about the event (e.g. files handled- or failure (e.g. error occurred and corrective action taken);
C. Which account and which administrator or operator was involved;
D. Which processes were involved.

System administrator and operator logs should be reviewed on a regular basis.

--- Page 157 ---

| T3.6.6 | FAULT LOGGING | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall log faults related to information processing or communication. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all faults to be captured in fault logs <br> 2) Identify minimum information requirements for each fault to be captured <br> 3) Define minimum frequency requirements for reviewing fault logs <br> 4) Ensure fault logs are reviewed and analyzed by personnel with appropriate training and skills <br> 5) Define minimum time requirements for maintaining fault logs |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Fault Logging enables systems to log and report faults (problems, errors or failures) related to information processing or communications. Faults reported by users or by system programs should be logged. There should be clear rules for handling reported faults including: <br> A. Review of fault logs to ensure that faults have been satisfactorily resolved; <br> B. Review of corrective measures to ensure that controls have not been compromised, and that the action taken is fully authorized. <br> It should be ensured that error logging is enabled, if this system function is available. |  |  |  |


| T3.6.7 | CLOCK <br> SYNCHRONIZATION | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall synchronize clocks of all relevant information systems with an agreed accurate time source. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define the date / time format and these Standards time to be used in all systems <br> 2) Define the stratum level of clocks needed for each type of network element <br> 3) Regularly check that the clocks of all relevant information processing systems are synchronized |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Where a computer or communications device has the capability to operate a real-time clock, this clock should be set to an agreed standard, e.g. Coordinated Universal Time (UTC- or local standard time. As some clocks are known to drift with time, there should be a procedure that checks for and corrects any significant variation. <br> The correct interpretation of the date/time format is important to ensure that the timestamp reflects the real date/time. Local specifics (e.g. daylight savings) should be taken into account. |  |  |  |  |

--- Page 158 ---

# T4 COMMUNICATIONS 

| T4 | COMMUNICATIONS |
| :-- | :-- |
| OBJECTIVE | To ensure the protection of information being exchanged within and <br> between entities |
| PERFORMANCE <br> INDICATOR | Frequency of breaches of information during communications |


| T4.1 | COMMUNICATIONS POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain a communications policy covering the security of information <br> shared internally and externally |
| PERFORMANCE <br> INDICATOR | Extent of communications policy deployment and adoption across the <br> entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable communications policy <br> - Unawareness of communications policy among IT staff |

--- Page 159 ---

|  T4.1.1 | COMMUNICATIONS
POLICY | PRIORITY | P3  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT  |
|  CONTROL | The entity shall establish a communications policy to guide the protection of information in transit. |  |   |
|  SUB-CONTROL | The communications policy shall:
1) Be appropriate to the purpose of the entity
2) Include statement of the management commitment, purpose, objective and scope of the policy
3) Outline the roles and responsibilities
4) Provide the framework to protect information in transit from interception, copying, modification, mis-routing, destruction, and other unauthorized activities
5) Be documented and communicated to all users
6) Be read and acknowledged formally by all users
7) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  The communications policy facilitates the implementation of the associated controls to secure information in transit and information sharing. The policy can, for example, contain in addition to the required sub-controls:
A. Information transfer procedures
B. Physical media transfer procedures
C. Electronic messaging
D. Information sharing protection
E. Network security management |  |  |   |
|  The communications policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |   |

--- Page 160 ---

| T4.2 | INFORMATION TRANSFER |
| :--: | :--: |
| OBJECTIVE | To maintain the security of information and software exchanged within an entity and with any external entity |
| PERFORMANCE INDICATOR | Percentage of people not complying with the information transfer policy |
| AUTOMATION GUIDANCE | Commercial DLP solutions are available to look for exfiltration attempts and detect other suspicious activities associated with a protected network holding sensitive information. Entities deploying such tools should carefully inspect their logs and follow up on any discovered attempts, even those that are successfully blocked, to transmit sensitive information out of the entity without authorization. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unprotected information in transit <br> - Tempering with information systems |


| T4.2.1 | INFORMATION <br> TRANSFER <br> PROCEDURES | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |
| CONTROL | The entity shall develop formal transfer procedures and controls should <br> be in place to protect the exchange of information. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish information transfer procedures <br> The procedures shall: <br> 2) Outline conditions under which the transfer of information must be <br> protected <br> 3) Identify specific controls to be put in place to ensure information is <br> adequately protected during transfer <br> 4) Identify actions to be taken when issues arise regarding the transfer <br> of information <br> 5) Be documented, maintained, reviewed and updated at planned <br> intervals or if significant changes occur |  |  |

--- Page 161 ---

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard.

The procedures and controls to be followed when using communication systems for information transfer should consider the following items:
A. Procedures designed to protect transferred information from interception, copying, modification, mis-routing and destruction
B. Procedures for the detection of and protection against malware that may be transmitted through the use of electronic communications
C. Procedures for protecting communicated sensitive or confidential electronic information that is in the form of an attachment
D. Policy or guidelines outlining acceptable use of communication systems
E. Personnel, external party and any other user's responsibilities not to compromise the entity, e.g. through defamation, harassment, impersonation, forwarding of chain letters, unauthorized purchasing, etc.
F. Use of cryptographic techniques e.g. to protect the confidentiality, integrity and authenticity of information
G. Retention and disposal guidelines for all business correspondence, including messages, in accordance with relevant national and local legislation and regulations
H. Controls and restrictions associated with using communication systems, e.g. automatic forwarding of electronic mail to external mail addresses
I. Advise personnel to take appropriate precautions not to reveal sensitive or confidential information
J. Not leaving messages containing sensitive or confidential information on answering machines since these may be replayed by unauthorized persons, stored on communal systems or stored incorrectly as a result of misdialing
K. Advise personnel about the problems of using facsimile machines, namely

1- Unauthorized access to built-in message stores to retrieve messages
2- Deliberate or accidental programming of machines to send messages to specific numbers
3- Sending documents and messages to the wrong number either by misdialing or using the wrong stored number
In addition, personnel should be reminded that they should not have confidential conversations in public places or over unsecure communication channels, open offices and meeting places. Information transfer services should comply with any relevant legal requirements.

--- Page 162 ---

| T4.2.2 | AGREEMENTS ON <br> INFORMATION <br> TRANSFER | PRIORITY |  |
| :-- | :-- | :-- | :-- | :-- |
| CONTROL | The entity shall establish agreements for the exchange of information <br> and software between the entity and external parties. |  |  |
|  | The entity shall: |  |  |
| SUB-CONTROL | 1) Identify all security requirements for exchanging information and <br> software with external parties <br> 2) Establish an exchange of information agreement with each external <br> party outlining clear roles and responsibilities of each party <br> 3) Ensure external parties are aware of all information security <br> requirements and policies that are necessary before signing <br> the agreement <br> 4) Monitor the exchange of information and software with external <br> parties to ensure the requirements in the agreement are being met <br> 5) Take corrective action when the exchange of information or <br> software does not follow the terms of the agreement |  |  |

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
Exchange agreements should consider the following security conditions:
A. Management responsibilities for controlling and notifying transmission, dispatch, and receipt;
B. Procedures for notifying sender of transmission, dispatch, and receipt;
C. Procedures to ensure traceability and non-repudiation;
D. Minimum technical standards for packaging and transmission;
E. Escrow agreements;
F. Courier identification standards;
G. Responsibilities and liabilities in the event of information security incidents, such as loss of data;
H. Use of an agreed labeling system for sensitive or critical information, ensuring that the meaning of the labels is immediately understood and that the information is appropriately protected;
I. Ownership and responsibilities for data protection, copyright, software license compliance and similar considerations;
J. Technical standards for recording and reading information and software;
K. Any special controls that may be required to protect sensitive items, such as cryptographic keys.

Policies, procedures, and standards should be established and maintained to protect information and physical media in transit (refer to T4.2.3), and should be referenced in such exchange agreements.

The security content of any agreement should reflect the sensitivity of the business information involved.

--- Page 163 ---

| T4.2.3 | PHYSICAL MEDIA <br> IN TRANSIT | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall protect physical media containing information during transportation. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify physical media carrying sensitive information <br> 2) Define labeling requirements for physical media carrying sensitive information <br> 3) Ensure physical media in transit carrying sensitive information is tracked sufficiently in accordance with the sensitivity of the information it contains <br> 4) Define measures to be taken in the event of loss of physical media in transit carrying sensitive information <br> 5) Keep a log of all transitions |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following guidelines should be considered to protect media containing information being transported between sites: <br> A. Reliable transport or couriers should be used <br> B. A list of authorized couriers should be agreed with management <br> C. Procedures to verify the identification of couriers should be developed <br> D. Packaging should be sufficient to protect the contents from any physical damage likely to arise during transit and in accordance with any manufacturers' specifications (e.g. for software), for example protecting against any environmental factors that may reduce the media's restoration effectiveness such as exposure to heat, moisture or electromagnetic fields <br> E. Logs should be kept, identifying the content of the media, the protection applied as well as recording the times of transfer to the transit custodians and the receipt at destination |  |  |  |

--- Page 164 ---

| T4.2.4 | ELECTRONIC <br> MESSAGING | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall protect information involved in electronic messaging.

SUB-CONTROL
The entity shall:

1) Identify all means of electronic messaging in which the entity's information assets can be transmitted
2) For each category of electronic messaging identified, define rules regarding the type of information that can be transmitted and specific controls needed
3) Develop the capability to monitor electronic messaging to ensure controls are implemented and the rules are followed
4) Take corrective action when information is transmitted through electronic messaging in a manner inconsistent with the established rules

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Security considerations for electronic messaging should include the following:
A. Protecting messages from unauthorized access, modification or denial of service
B. Ensuring correct addressing and transportation of the message
C. General reliability and availability of the service
D. Legal considerations, for example requirements for electronic signatures
E. Obtaining approval prior to using external public services such as instant messaging or file sharing
F. Stronger levels of authentication controlling access from publicly accessible networks

--- Page 165 ---

| T4.2.5 | BUSINESS <br> INFORMATION <br> SYSTEMS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall develop policies and procedures to protect information transferred across business information systems. |  |  |  |
| SUB-CONTROL | The policies and procedures shall: <br> 1) Identify all points of interconnection between business information systems <br> 2) Identify the types of information to be protected regarding the identified interconnections <br> 3) Identify appropriate security measures to be taken to protect each type of information <br> 4) Be documented, maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Consideration given to the security and business implications of interconnecting such systems should include: <br> A. Known vulnerabilities in the administrative and accounting systems where information is shared between different parts of the entity <br> B. Vulnerabilities of information in business communication systems, e.g. recording phone calls or conference calls, confidentiality of calls, storage of facsimiles, opening mail, distribution of mail <br> C. Policy and appropriate controls to manage information sharing <br> D. Excluding categories of sensitive business information and classified documents if the system does not provide an appropriate level of protection <br> E. Restricting access to diary information relating to selected individuals, e.g. personnel working on sensitive projects <br> F. Categories of personnel, contractors or business partners allowed to use the system and the locations from which it may be accessed <br> G. Restricting selected systems to specific categories of user <br> H. Identifying the status of users, e.g. employees of the entity or contractors in directories for the benefit of other users <br> I. Retention and backup of information held on the system <br> J. Fallback requirements and arrangements |  |  |  |  |

--- Page 166 ---

| T4.3 | ELECTRONIC COMMERCE SERVICES |
| :-- | :-- |
| OBJECTIVE | To ensure the security of electronic commerce services |
| PERFORMANCE <br> INDICATOR | Percentage of e-commerce volume subject to information security <br> incidents |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Embezzlement, skimming, and related fraud <br> - Eavesdropping / Packet Sniffing |


| T4.3.1 | ELECTRONIC <br> COMMERCE | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |
| CONTROL | The entity shall protect information involved in electronic commerce <br> passing over public networks from fraudulent activity, contract dispute, <br> and unauthorized disclosure and modification. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all instances of electronic commerce within the entity that <br> require passing information over public networks <br> 2) Identify appropriate security measures for information passing over <br> public networks based on the risk assessment <br> 3) Ensure security requirements are captured in service agreements <br> with e-commerce partners <br> 4) Monitor e-commerce activities for on-going compliance with security <br> requirements |  |  |

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
Security considerations for electronic commerce should include the following:
A. The level of confidence each party requires in each other's claimed identity, e.g. through authentication
B. Authorization processes associated with who may set prices, issue or sign key trading documents
C. Ensuring that trading partners are fully informed of their authorizations
D. Determining and meeting requirements for confidentiality, integrity, proof of dispatch and receipt of key documents, and the non-repudiation of contracts, e.g. associated with tendering and contract processes
E. The level of trust required in the integrity of advertised price lists
F. The confidentiality of any sensitive data or information
G. The confidentiality and integrity of any order transactions, payment information, delivery address details, and confirmation of receipts
H. The degree of verification appropriate to check payment information supplied by a customer
I. Selecting the most appropriate settlement form of payment to guard against fraud

--- Page 167 ---

J. The level of protection required to maintain the confidentiality and integrity of order information
K. Avoidance of loss or duplication of transaction information;
L. Llability associated with any fraudulent transactions;
M. Insurance requirements.

Many of the above considerations can be addressed by the application of cryptographic controls taking into account compliance with legal requirements.

Electronic commerce arrangements between trading partners should be supported by a documented agreement which commits both parties to the agreed terms of trading, including details of authorization (see b- above). Other agreements with information service and value added network providers may be necessary.

Public trading systems should publicize their terms of business to customers. Consideration should be given to the resilience to attack of the host(s) used for electronic commerce, and the security implications of any network interconnection required for the implementation of electronic commerce services.

| T4.3.2 | ON-LINE <br> TRANSACTIONS | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall protect information involved in on-line transactions against incomplete transmission, mis-routing, unauthorized message alteration, unauthorized disclosure, unauthorized message duplication or replay. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all information used in on-line transactions <br> 2) Identify appropriate security measures for information used in online transactions based on the risk assessment <br> 3) Ensure security requirements are captured in service agreements with all partners involved in on-line transactions <br> 4) Monitor on-line transactions for on-going compliance with security requirements |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Security considerations for on-line transactions should include the following: <br> A. The use of electronic signatures by each of the parties involved in the transaction <br> B. All aspects of the transaction, i.e. ensuring that <br> 1- User credentials of all parties are valid and verified <br> 2- The transaction remains confidential <br> 3- Privacy associated with all parties involved is retained <br> C. Communications path between all involved parties is encrypted <br> D. Protocols used to communicate between all involved parties is secured <br> E. Ensuring that the storage of the transaction details are located outside of any public accessible environment, e.g. on a storage platform existing on the organizational Intranet, and not retained and exposed on a storage medium directly accessible from the Internet <br> F. Where a trusted authority is used (e.g. for the purposes of issuing and maintaining digital signatures and/or digital certificates) security is integrated and embedded throughout the entire end-to-end certificate/signature management process |  |  |  |

--- Page 168 ---

| T4.3.3 | PUBLICLY AVAILABLE <br> INFORMATION | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall protect information being made available on a publicly available system against unauthorized modification. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all information to be made available on a publicly available system <br> 2) Define security requirements for information to be made available on a publicly available system based on the risk assessment <br> 3) Monitor information being made available on publicly available systems for unauthorized modification <br> 4) Ensure that all public information is sanitized and approved |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. <br> Software, data, and other information requiring a high level of integrity, being made available on a publicly available system, should be protected by appropriate mechanisms, e.g. digital signatures. The publicly accessible system should be tested against weaknesses and failures prior to information being made available. <br> There should be a formal approval process before information is made publicly available. In addition, all input provided from the outside to the system should be verified and approved. <br> Electronic publishing systems, especially those that permit feedback and direct entering of information, should be carefully controlled so that: <br> A. Information is obtained in compliance with any data protection legislation <br> B. Information input to, and processed by, the publishing system will be processed completely and accurately in a timely manner <br> C. Sensitive information will be protected during collection, processing, and storage <br> D. Access to the publishing system does not allow unintended access to networks to which the system is connected |  |  |  |  |

--- Page 169 ---

| T4.4 | INFORMATION SHARING PROTECTION |
| :-- | :-- |
| OBJECTIVE | To ensure adequate protection of information shared within an information <br> sharing community |
| PERFORMANCE <br> INDICATOR | Frequency of information security incidents occurring within each <br> information sharing community in which information is intentionally or <br> unintentionally disclosed |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Misappropriation of private knowledge <br> - Abuse of system access/privileges |


| T4.4.1 | CONNECTIVITY <br> TO INFORMATION <br> SHARING <br> PLATFORMS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall ensure that connectivity to information sharing platforms should be secured. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all relevant information sharing platforms to which the entity will connect <br> 2) Determine the security requirements for connecting to identified platforms <br> 3) Identify specific controls needed to meet the security requirements for each information sharing platform <br> 4) Develop the capabilities needed for secure connectivity to any required sector, national, or international information sharing communities |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard (also refer to National Cyber Information Sharing Policy). |  |  |  |  |
| While most information sharing communities are built on a voluntary basis, certain entities may also have mandatory requirements to join specific information sharing platforms (e.g. sector or national level platforms established by regulators or other national authorities). |  |  |  |  |
| In all cases, it is the responsibility of the information sharing platform manager to outline minimum security requirements for all information sharing community members. This helps install a basic component of trust that all community members have the minimum security controls in place to protect the information being shared on the platform. |  |  |  |  |
| Entities looking to connect to information sharing platforms should contact the platform manager for security requirements and ensure all requirements are fully understood and implemented. |  |  |  |  |

--- Page 170 ---

| T4.4.2 | INFORMATION <br> RELEASED INTO <br> INFORMATION <br> SHARING <br> COMMUNITIES | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall follow the format, classification, and treatment requirements of the information sharing community for information released into information sharing communities. |  |  |  |
| SUB-CONTROL | For each connected information sharing platform, the entity shall: <br> 1) Identify all information to be released into the information sharing community utilizing the platform <br> 2) Implement minimum format, classification, and treatment requirements as outlined by the platform manager <br> 3) Identify and implement any additional security requirements needed to protect the released information in line with the entity's risk assessment <br> 4) Develop the capabilities needed to share information securely within any required sector, national or international information sharing communities |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard (also refer to National Cyber Information Sharing Policy). <br> Based on urgency, potential consequences and technical constraints, it may not be possible for an entity to validate all information before transmission into the information sharing community. Where limitations exist, these should be indicated as part of the message. Also, indicating reservations on credibility of information is particularly important where the source is anonymous or unknown. It is important to indicate where the originator has been able to validate the information given directly, and can vouch for its authenticity. <br> There are technical mechanisms that can be used to provide authenticity without compromising anonymity. For example, shared cryptographic secrets could be used to confirm that a communication originated from a member of the community without revealing the actual identity of the originator. <br> Each recipient should be responsible for obtaining any necessary authorizations for wider release from the originator prior to onwards distribution. <br> In inter-sector communications, the originator may not know who all the entities that receive the information will be. In such a case, a general or specific sector release approval will need to be granted. <br> In addition, all information sharing communities should define rules for the protection of information in transit, and only permit members to join the community if such rules are accepted and implemented by the prospective member. Any supporting entity should implement such rules internally. <br> Information sharing communities should consider implementing alternative mechanisms for information sharing that do not rely on electronic messaging, and enabling members to specify that specific messages are distributed by such other routes. |  |  |  |  |

--- Page 171 ---

| T4.5 | NETWORK SECURITY MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure the protection of information in networks and the protection of the <br> supporting infrastructure |
| PERFORMANCE <br> INDICATOR | Percentage of information systems that meet all network security <br> management requirements |
| AUTOMATION <br> GUIDANCE | Port scanning tools are used on a range of target systems to determine <br> which services are listening on the network. In addition to determining which <br> ports are open, effective port scanners can be configured to identify the <br> version of the protocol and service listening on each discovered open port. <br> This list of services and their versions are compared against an inventory of <br> services required by the entity for each server and workstation in an asset <br> management system. Recently added features in these port scanners <br> are being used to determine the changes in services offered by scanned <br> machines on the network since the previous scan, helping security personnel <br> identify differences over time. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Abuse of system access/privileges <br> - Eavesdropping / Packet Sniffing <br> - Denial of Service (DOS) or DDOS |

--- Page 172 ---

| T4.5.1 | NETWORK <br> CONTROLS | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall ensure that all networks are adequately managed, controlled, and protected. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all network components and interconnectivity between them <br> 2) Document and maintain network diagram that includes all network components as well as their connections <br> 3) Perform a risk assessment on individual network components and the network as a whole to identify vulnerabilities requiring action <br> 4) Identify and implement specific network controls needed to mitigate the vulnerabilities identified <br> 5) Continually monitor the in-place controls for efficiency and effectiveness |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Network managers should implement controls to ensure the security of information in networks, and the protection of connected services from unauthorized access. In particular, the following items should be considered: <br> A. Operational responsibility for networks should be separated from computer operations where appropriate <br> B. Responsibilities and procedures for the management of remote equipment, including equipment in user areas, should be established <br> C. Special controls may be required to maintain the availability of the network services and computers connected <br> D. Management activities should be closely coordinated both to optimize the service to the entity and to ensure that controls are consistently applied across the information processing infrastructure |  |  |  |
| Further measures can include: <br> E. Implement ingress and egress filtering to allow only those ports and protocols with an explicit and documented business need <br> F. Restrict access only to trusted sites (white lists) <br> G. Inspect packets on DMZ networks using Security Event Information Management (SEIM) or log analytics systems <br> H. Deploy Sender Policy Framework (SPF) records in DNS and enabling receiver-side verification in mail servers <br> I. Disable / uninstall unused services; <br> J. Enable host-based firewalls or port filtering tools on end systems with a default-deny rule that drops all traffic except those services and ports that are explicitly allowed <br> K. Regularly scan port on all key servers, and compare results to a known effective baseline <br> L. Backup and protect firewall, router, and switch configurations |  |  |  |

--- Page 173 ---

| T4.5.2 | SECURITY OF <br> NETWORK SERVICES | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall identify the security features, service levels, and management requirements of all network services and include these requirements in any network services agreement, whether these services are provided in-house or outsourced. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Specify which network services are subject to specific security requirements <br> 2) Define minimum security requirements for each identified service <br> 3) Ensure minimum security requirements are captured in service level agreements for network services <br> 4) Ensure minimum security requirements are implemented in network services |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The ability of the network service provider to manage agreed services in a secure way should be determined and regularly monitored, and the right to audit should be agreed. |  |  |  |
| The security arrangements necessary for particular services, such as security features, service levels, and management requirements, should be identified. The entity should ensure that network service providers implement these measures. |  |  |  |

--- Page 174 ---

| T4.5.3 | SEGREGATION IN <br> NETWORKS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
| APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |  |

CONTROL The entity shall segregate groups of information services, users, and information systems on networks.

SUB-CONTROL
The entity shall:

1) Identify criteria for grouping information services, users, and information systems into different groups that facilitate segregation on networks
2) For each group, identify specific segregation requirements
3) Ensure identified segregation requirements are included in the relevant system / service development lifecycle
4) Periodically evaluate the effectiveness of implemented segregation strategies and identify areas for improvement

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

One method of controlling the security of large networks is to divide them into separate logical network domains, e.g. an entity's internal network domains and external network domains, each protected by a defined security perimeter. A graduated set of controls can be applied in different logical network domains to further segregate the network security environments, e.g. publicly accessible systems, internal networks, and critical assets. The domains should be defined based on a risk assessment and the different security requirements within each of the domains.

Such a network perimeter can be implemented by installing a secure gateway between the two networks to be interconnected to control access and information flow between the two domains. This gateway should be configured to filter traffic between these domains and to block unauthorized access in accordance with the entity's access control policy. An example of this type of gateway is what is commonly referred to as a firewall. Another method of segregating separate logical domains is to restrict network access by using virtual private networks for user groups within the entity.

Networks can also be segregated using the network device functionality, e.g. IP switching. Separate domains can then be implemented by controlling the network data flows using the routing/switching capabilities, such as access control lists.

The criteria for segregation of networks into domains should be based on the access control policy and access requirements, and also take account of the relative cost and performance impact of incorporating suitable network routing or gateway technology.

In addition, segregation of networks should be based on the value and classification of information stored or processed in the network, levels of trust, or lines of business, in order to reduce the total impact of a service disruption.

--- Page 175 ---

| T4.5.4 | SECURITY OF <br> WIRELESS <br> NETWORKS | PRIORITY <br> APPLICABILITY | P2 <br> BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall ensure that all wireless networks are adequately secured. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Undertake and document a site survey to determine the optimal physical locations to avoid stray signal leaking too far outside of the entity's physical perimeter <br> 2) Identify criteria for grouping information services, users, and information systems into different groups that facilitate segregation on wireless networks <br> 3) For each wireless network, identify the security controls that should be in place based on the required protection level of the information services, users, and information systems it supports <br> 4) Periodically evaluate the effectiveness of implemented segregation strategies and identify areas for improvement |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Consideration should be given to the segregation of wireless networks from internal and private networks. As the perimeters of wireless networks are not well defined, a risk assessment should be carried out in such cases to identify controls (e.g. strong authentication, cryptographic methods, and frequency selection) to maintain network segregation. |  |  |  |
| When designing its wireless networks, the entity should consider the number of base stations to be deployed, where they will be situated, what bandwidth limitations should apply to clients and what wired alternatives should exist, so as to limit the potential for wireless-based Denial of Service attacks. |  |  |  |
| The use of 'guest' wireless networks should be restricted to genuine short-term guests of the Entity and consultants without a verified need for connection to the Entity's core network. Guest networks should only connect to the Internet and their data should not transit via the Entity's core network. Traffic on wireless guest networks should not be terminated on the core network and should be tunnelled directly to the network perimeter. |  |  |  |
| Traffic on guest networks should be monitored by the entity to ensure conformance with its acceptable usage provisions. Temporary users of guest networks should be required to authenticate to the network, to avoid opportunistic use of the Entity's network resources. |  |  |  |
| Network managers should implement controls to ensure the security of information in wireless. In particular, special controls should be established to safeguard the confidentiality and integrity of data passing over wireless networks, and to protect the connected systems and applications. |  |  |  |
| The entity should prohibit and sanction the creation and use of ad-hoc wireless networks, including the connecting of unapproved wireless base-stations to the entity's core data network. |  |  |  |
| The entity should put in place mechanisms that allow for the identification and isolation of rogue wireless access points. |  |  |  |

--- Page 176 ---

# T5 ACCESS CONTROL 

| T5 | ACCESS CONTROL |
| :-- | :-- |
| OBJECTIVE | To institute access control at the user, application, network and <br> operating system level as well as for mobile computing |
| PERFORMANCE <br> INDICATOR | Number of blocked attempts at unauthorized access |


| T5.1 | ACCESS CONTROL POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain an access control policy covering user authorization procedures <br> to information assets |
| PERFORMANCE <br> INDICATOR | Extent of access control policy deployment and adoption across the <br> entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | Unsuitable access control policy <br> - Unawareness of access control policy among IT staff |


| T5.1.1 | ACCESS CONTROL <br> POLICY | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL
The entity shall establish an access control policy based on business and security requirements.

SUB-CONTROL
The access control policy shall:

1) Be appropriate to the purpose of the entity
2) Include statement of the management commitment, purpose, objective and scope of the policy
3) Outline the roles and responsibilities for granting and denying access
4) Provide the framework for the protection of mobile devices against prevailing risks, including users owned devices
5) Provide the framework to protect information from unauthorized access and grant access to the appropriate users and mobile devices
6) Be documented and communicated to all users
7) Be read and acknowledged formally by all users
8) Be maintained, reviewed and updated at planned intervals or if significant changes occur

--- Page 177 ---

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Asset owners should determine appropriate access rules, privileges and restrictions for specific user roles towards their assets, with the amount of detail and the strictness of the controls reflecting the associated information security risks.

Users and service providers should be given a clear statement of the business requirements to be met by access controls.
The policy should take account of the following:
A. Security requirements of individual business applications
B. Policies for information dissemination and authorization, e.g. the need to know principle and security levels and classification of information
C. Consistency between the access rights and information classification policies of different systems and networks
D. Relevant legislation and any contractual obligations regarding protection of access to data or services
E. Management of access rights for users and mobile devices in a distributed and networked environment which recognizes all types of connections available
F. Segregation of access control roles, e.g. access request, access authorization, access administration
G. Requirements for formal authorization of access requests
H. Requirements for periodic review of access controls
I. Removal of access rights related to users and mobile devices
J. Archiving of records of all significant events concerning the use and management of user identities and security credentials
K. Privileged access roles

When using mobile devices, e.g. notebooks, palmtops, laptops, smart cards, and mobile phones, special care should be taken to ensure that business information is not compromised. The access control policy should take into account the risks of working with mobile computing equipment in unprotected environments.

The mobile related requirements should include physical protection, access controls, cryptographic techniques, backups, and virus protection. This policy should also include rules and advice on connecting mobile devices to networks and guidance on the use of these facilities in public places.

--- Page 178 ---

|  T5.2 | USER ACCESS MANAGEMENT  |
| --- | --- |
|  OBJECTIVE | To ensure authorized user access and to prevent unauthorized access to information systems  |
|  PERFORMANCE INDICATOR | Number of delayed access change requests, and when they have been actioned  |
|  AUTOMATION GUIDANCE | One way of automation is to use identity management systems to manage accounts, their authentication, authorization, roles, and privileges. They are available for entities of all sizes and complexity. Selection of the appropriate identity management system requires an entity to understand its technology landscape, integration requirements, and maturity of its IT staff.
Entity should consider which authentication technologies and processes to apply, including smart cards, security tokens, one time passwords, security authentications apps for smartphones, biometric authentication systems, etc.  |
|  RELEVANT
THREATS AND
VULNERABILITIES | - Use of stolen login credentials
- Brute force and dictionary attacks
- Authentication bypass  |

--- Page 179 ---

| T5.2.1 | USER REGISTRATION | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall implement a formal user registration and de-registration procedure. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish and formalize procedures for the registration and deregistration of users <br> 2) Ensure that a separate account is created for each person requiring access, and prohibit sharing of same accounts across multiple users <br> 3) Immediately revoke access from users who have changed roles or jobs or left the entity following the established procedure <br> 4) Periodically check and revoke access related to temporary and inactive accounts |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The access control procedure for user registration and de-registration should include: <br> A. Using unique user IDs to enable users to be linked to and held responsible for their actions; the use of shared IDs should only be permitted where they are necessary for business or operational reasons and should be approved and documented <br> B. Verifying that the user has authorization from the owner of the information system or service for the use of the information system or service; separate approval for access rights from management may also be appropriate <br> C. Verifying that the level of access granted is appropriate to the business purpose and is consistent with organizational security policy, e.g. it does not compromise segregation of duties <br> D. Ensuring service providers do not provide access until authorization procedures have been completed <br> E. Maintaining a formal record of all persons registered to use systems and service centrally <br> F. Immediately removing or blocking access rights of users who have changed roles or jobs or left the entity <br> G. Periodically identifying, and removing or blocking, redundant user IDs and redundant and inactive accounts <br> H. Ensuring that redundant user IDs are not issued to other users |  |  |

--- Page 180 ---

| T5.2.2 | PRIVILEGE <br> MANAGEMENT | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall restrict and control the allocation and use of privileges.

SUB-CONTROL
The entity shall:

1) Maintain a record of all allocated privileges
2) Never grant users with domain or local administrative privileges
3) Ensure that administrator accounts are used only for system administration activities (e.g. no email or web surfing)
4) Use two-factor authentication for all administrative access
5) Ensure that all administrative access are logged and audited

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Multi-user systems that require protection against unauthorized access should have the allocation of privileges controlled through a formal authorization process in accordance with the relevant access control policy. The following steps should be considered:
A. Identify privileged access rights associated with each system, e.g. operating system, database and application
B. Privileged access rights should:

- Be allocated to users on a need-to-use basis and on an event-by-event basis in line with the access control policy, i.e. the minimum requirement for their functional role only when needed
- Not be granted until the authorization process is complete
- Be assigned to a different User ID than the User ID used for day to day work. Regular user activities should not be performed from privileged accounts
C. An authorization process and a record of all privileges allocated should be maintained;
D. Requirements for expiry of privileged access rights should be defined
E. The competences of users with privileged access rights should be reviewed regularly in order to verify if they are in line with their duties
F. Specific procedures should be established and maintained in order to avoid the use of generic administration User IDs, according to systems configuration capabilities
G. For generic administration User IDs, the confidentiality of security credentials should be maintained when shared (changing them frequently and as soon as possible when a privileged user leaves or changes job, communicating them among privileged users with appropriate mechanisms)

--- Page 181 ---

| T5.2.3 | USER SECURITY <br> CREDENTIALS <br> MANAGEMENT | PRIORITY <br> APPLICABILITY | P1 <br> BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall control the allocation of user security credentials. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish a user security credential management policy for users and administrators that is appropriate to the purpose of the entity <br> 2) Ensure that the policy includes a secure process to provide users with security credentials; policy should also include credential revocation procedure and credential re-allocation. <br> 3) In case of use of security credentials (i.e. passwords) change default security credentials of all systems and applications <br> 4) In case of credentials, always store them in a well-hashed (including "salting") or encrypted format <br> 5) For accessing critical resources/assets, implement credential systems based on multi-factor authentication |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The process should include the following requirements: <br> A. Users should be required to sign a statement to keep personal security credentials confidential and to keep group e.g. security credentials solely within the members of the group; this signed statement could be included in the terms and conditions of employment <br> B. When users are required to maintain their own security credentials they should be provided initially with secure temporary security credentials, which they are forced to change immediately <br> C. Establish procedures to verify the identity of a user prior to providing a new, replacement or temporary security credentials <br> D. Temporary security credentials should be given to users in a secure manner; the use of external parties or unprotected (clear text) electronic mail messages should be avoided <br> E. Temporary security credentials should be unique to an individual and should not be guessable <br> F. Users should acknowledge receipt of security credentials <br> G. Default vendor security credentials should be altered following installation of systems or software. |  |  |  |

--- Page 182 ---

| T5.2.4 | REVIEW OF USER <br> ACCESS RIGHTS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall review users' access rights. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Maintain access right records for all assets, and identify any granted <br> special access <br> 2) Establish a access right review procedure to ensure access rights <br> are reviewed periodically or on any changes in users' status <br> 3) Periodically check the granted special access to ensure their validity |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The review of access rights should consider the following guidelines: <br> A. Users' access rights should be reviewed at regular intervals and after any changes, such as <br> promotion, demotion or termination of employment <br> B. User access rights should be reviewed and re-allocated when moving from one employment <br> to another within the same entity <br> C. Authorizations for special privileged access rights should be reviewed at more <br> frequent intervals <br> D. Privilege allocations should be checked at regular intervals to ensure that unauthorized <br> privileges have not been obtained <br> E. Changes to privileged accounts should be logged for periodic review |  |  |  |


| T5.3 | USER RESPONSIBILITIES |
| :-- | :-- |
| OBJECTIVE | To prevent unauthorized user access, and compromise or theft of information <br> and information systems |
| PERFORMANCE <br> INDICATOR | Percentage of users compliant with the users rules of behavior (such as <br> password policy, clean desk policy) |
| AUTOMATION <br> GUIDANCE | For password management, built-in operating system features for <br> minimum password length can be configured that prevent users from <br> choosing short passwords. To enforce password complexity (requiring <br> passwords to be a string of pseudo-random characters), built-in operating <br> system settings or third-party password complexity enforcement tools can <br> be applied. For critical information and services, two factor authentication <br> systems should be considered. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Intentional leaks and sharing of data by staff <br> - Illegal processing of data <br> - Abuse of system access and/or privileges |

--- Page 183 ---

| T5.3.1 | USE OF SECURITY <br> CREDENTIALS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall require users to use security credentials in line with the entity's security practices.

SUB-CONTROL The entity shall:

1) Develop a good practice for use of security credentials
2) Share and educate users on the developed good practices through awareness and training sessions (refer to M3.2.1)

IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)
All users should be advised to:
A. Keep secret authentication confidential, ensuring that they are not divulged to any other parties, including people of authority;
B. Avoid keeping a record (e.g. paper, software file or hand-held device- of security credentials, unless this can be stored securely and the method of storing has been approved (e.g. password vault);
C. Change security credentials whenever there is any indication of their possible compromise;
D. When passwords are used as security credentials, select quality passwords with sufficient minimum length which are:

1) Easy to remember
2) Not based on anything somebody else could easily guess or obtain using person related information, e.g. names, telephone numbers and dates of birth etc.;
3) Not vulnerable to dictionary attacks (i.e. do not consist of words included in dictionaries)
4) Free of consecutive identical, all-numeric or all-alphabetic characters
E. Change temporary passwords at the first log-on
F. Not share individual user's security credentials
G. When passwords are used as security credentials in automated logon procedures, these should not be stored without proper protection
H. Not use the same security credentials for business and non-business purposes

If users need to access multiple services, systems or platforms, and they are required to maintain multiple separate passwords, they should be advised that they may use a single, quality password (see d) for all services where the user is assured that a reasonable level of protection has been established for the storage of the password within each service, system or platform.

--- Page 184 ---

| T5.4 | NETWORK ACCESS CONTROL |
| :--: | :--: |
| OBJECTIVE | To prevent unauthorized access to networked services |
| PERFORMANCE INDICATOR | Firewall statistics, such as percentage of outbound packets or sessions that are blocked (e.g. attempted access to blacklisted websites; number of potential hacking attacks repelled, categorized into trivial/of some concern/critical) |
| AUTOMATION GUIDANCE | Some entities use commercial tools that evaluate the rule set of network filtering devices to determine whether they are consistent or in conflict, providing an automated sanity check of network filters and search for errors in rule sets or access controls lists (ACLs) that may allow unintended services through the device. Such tools should be run each time significant changes are made to firewall rule sets, router ACLs, or other filtering technologies. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unauthorized access to network services by internal or external user <br> - KeyLogger / Form-Grabber / Spyware <br> - Tampering in network utilities |


| T5.4.1 | POLICY ON USE OF <br> NETWORK SERVICES | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall provide access to users only to the services that they <br> have been specifically authorized to use. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish a policy for the use of network services that is appropriate <br> to the entity <br> 2) Develop the framework for managing the network services and <br> ensure the right level of protection provided against unauthorized <br> access <br> 3) Limit user access to the required network services and in line with the <br> developed framework |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| A policy should be formulated concerning the use of networks and network services. This policy <br> should cover: <br> A. The networks and network services which are allowed to be accessed; <br> B. Authorization procedures for determining who is allowed to access which networks and <br> networked services <br> C. Management controls and procedures to protect access to network connections and <br> network services <br> D. The means used to access networks and network services (e.g. use of VPN or wireless <br> network) <br> E. The policy on the use of network services should be consistent with the entities access <br> control policy |  |  |  |

--- Page 185 ---

| T5.4.2 | USER <br> AUTHENTICATION <br> FOR EXTERNAL <br> CONNECTIONS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall use appropriate authentication methods to control access of remote users.

SUB-CONTROL
The entity shall:

1) Require all remote login (users and administrators) to be done over secure channels
2) Ensure appropriate authentication methods to be used to control access by remote users
3) Block access to a machine (either remotely or locally) for administrator-level accounts

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Authentication of remote users can be achieved using, for example, a cryptographic based technique, hardware tokens, or a challenge/response protocol. Possible implementations of such techniques can be found in various virtual private networks (VPN solutions). Dedicated private lines can also be used to provide assurance of the source of connections.

Node authentication can serve as an alternative means of authenticating groups of remote users where they are connected to a secure, shared computer facility. Cryptographic techniques, e.g. based on machine certificates, can be used for node authentication. This is part of several VPN based solutions.

| T5.4.3 | EQUIPMENT <br> IDENTIFICATION IN <br> NETWORKS | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall be able to identify equipment connected to its networks.

SUB-CONTROL
The entity shall:

1) Use equipment identification mechanisms to automatically authenticate legitimate connections and detect unauthorized devices connected to the network

## IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)

Equipment identification can be used if it is important that the communication can only be Equipment identification can be used if it is important that the communication can only be initiated from a specific location or equipment. An identifier in or attached to, the equipment can be used to indicate whether this equipment is permitted to connect to the network. These identifiers should clearly indicate to which network the equipment is permitted to connect, if more than one network exists and particularly if these networks are of differing sensitivity. It may be necessary to consider physical protection of the equipment to maintain the security of the equipment identifier.

--- Page 186 ---

| T5.4.4 | REMOTE <br> DIAGNOSTIC AND <br> CONFIGURATION <br> PROTECTION | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall control access for the purpose of diagnostic and configuration. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all ports and services that are used for diagnostic or configuration <br> 2) Disable or uninstall the diagnostic and configuration services that are not required and define a protection mechanism for the ones that are required <br> 3) Enable access control mechanisms (including strong authentication) to allow access only to authorized personnel <br> 4) Log all remote access activities related to diagnostic and configuration |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Many computer systems, network systems, and communication systems are installed with a remote diagnostic and configuration port or service for use by maintenance engineers. If unprotected, these diagnostic ports provide a means of unauthorized access. |  |  |  |  |


| T5.4.5 | NETWORK <br> CONNECTION <br> CONTROL | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall restrict user access to shared networks. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish a procedure to provide access to shared networks in <br> line with Access Control Policy and requirements of the business <br> applications (refer to T5.1.1) <br> 2) Restrict users access to the network based on predefined tables and <br> rules (e.g. certain time of the day) |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The network access rights of users should be maintained and updated as required by the access <br> control policy. The connection capability of users can be restricted through network gateways <br> that filter traffic by means of pre-defined tables or rules. Examples of applications to which <br> restrictions should be appTlied are: <br> A. Messaging, e.g. electronic mail <br> B. File transfer <br> C. Interactive access <br> D. Application access <br> Linking network access rights to certain times of day or dates should be considered. |  |  |  |

--- Page 187 ---

| T5.4.6 | NETWORK ROUTING <br> CONTROL | PRIORITY <br> APPLICABILITY | P3 <br> BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall implement network routing controls to ensure that computer connections and information flows do not breach the access control policy of the business applications. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify all routing equipment (e.g. routers, firewalls, and switches.) (refer to T1.2.1) <br> 2) Establish a secure configuration and rules for network routing (refer to T3.2.1) <br> 3) Enable source and destination address violation against rules checking on the routing equipment <br> 4) Enable routing protection countermeasures to avoid manipulation of routing systems/tables <br> 5) Implement sub-networks for publicly accessible systems that are separated from internal organizational networks (refer to T4.5.3) <br> 6) Connect to external networks or information systems only through managed interfaces consisting of boundary protection devices (such as firewalls) <br> 7) Monitor communications with external systems and with key internal systems for suspicious traffic |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Routing controls should be based on positive source and destination address checking mechanisms. |  |  |  |
| Managed interfaces include, for example, gateways, routers, firewalls, guards, network-based malicious code analysis and virtualization systems, or encrypted tunnels implemented within a security architecture (e.g., routers protecting firewalls or application gateways residing on protected sub-networks). Sub-networks that are physically or logically separated from internal networks are referred to as demilitarized zones or DMZs. Restricting or prohibiting interfaces within organizational information systems includes, for example, restricting external web traffic to designated web servers within managed interfaces and prohibiting external traffic that appears to be spoofing internal addresses. |  |  |  |

--- Page 188 ---

| T5.4.7 | WIRELESS ACCESS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall ensure wireless access is secured. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish usage restrictions, configuration requirements, and implementation guidance for wireless access <br> 2) Authorize wireless access to the information system prior to allowing such connections |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Wireless technologies include, for example, microwave, packet radio (UHF/VHF), 802.11x, and Bluetooth. Wireless networks use authentication protocols (e.g., EAP/TLS, PEAP), which provide credential protection and mutual authentication. <br> Authentication controls should be implemented to control access to wireless networks. In particular, special care is needed in the selection of controls for wireless networks due to the greater opportunities for undetected interception and insertion of network traffic. <br> Entities should consider a number of actions to limit unauthorized use of wireless communications outside its boundaries include, for example: <br> - Reducing the power of wireless transmissions so that the transmissions are less likely to emit a signal that can be used by adversaries outside of the physical perimeters of organizations <br> - Employing measures such as TEMPEST to control wireless emanations <br> - Using directional/beam forming antennas that reduce the likelihood that unintended receivers will be able to intercept signals <br> Prior to taking such actions, entities can conduct periodic wireless surveys to understand the radio frequency profile of its information systems as well as other systems that may be operating in the area. |  |  |

--- Page 189 ---

| T5.5 | OPERATING SYSTEM ACCESS CONTROL |
| :--: | :--: |
| OBJECTIVE | To prevent unauthorized access to operating systems |
| PERFORMANCE INDICATOR | Number of blocked attempts at unauthorized access to operating systems |
| AUTOMATION GUIDANCE | Built-in operating system features can extract lists of accounts with super-user privileges, both locally on individual systems and on overall domain controllers. To verify that users with high-privileged accounts do not use such accounts for day-to-day web surfing and e-mail reading, security personnel should periodically gather a list of running processes to determine whether any browsers or e-mail readers are running with high privileges. Such information gathering can be scripted, with short shell scripts searching for a dozen or more different browsers, e-mail readers, and document editing programs running with high privileges on machines. Some legitimate system administration activity may require the execution of such programs over the short term, but long-term or frequent use of such programs with administrative privileges could indicate that an administrator is not adhering to this control. Monitoring tools can provide such information. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Abuse of system access/privileges <br> - Backdoor or Command and Control <br> - Disable or interfere with security controls <br> - Tampering in network utilities |

--- Page 190 ---

| T5.5.1 | SECURE LOG-ON <br> PROCEDURES | PRIORITY | P1 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall control access to systems and applications using a secure log-on and log-off procedure. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the systems, applications and services that require user authentication <br> 2) Classify the identified systems, application and services based on the level of protection needed <br> 3) Establish the appropriate log-on and log-off procedures to minimize the opportunity for unauthorized access <br> 4) Set a maximum session time for logged on users for sensitive systems and applications <br> 5) Terminate inactive sessions after a predefined period of inactivity |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Eventhough mostapplications have securelog-onimplemented, a suitable authenticationtechnique should be chosen to substantiate the claimed identity of a user. Where strong authentication and identity verification is required, authentication methods alternative to passwords, such as cryptographic means, smart cards, tokens or biometric means, should be used. |  |  |  |
| The procedure for logging into a system or application should be designed to minimize the opportunity for unauthorized access. The log-on procedure should therefore disclose the minimum of information about the system or application, in order to avoid providing an unauthorized user with any unnecessary assistance. A good log-on procedure should: <br> A. Not display system or application identifiers until the log-on process has been successfully completed <br> B. Display a general notice warning that the computer should only be accessed by authorized users <br> C. Not provide help messages during the log-on procedure that would aid an unauthorized user <br> D. Validate the log-on information only on completion of all input data. If an error condition arises, the system should not indicate which part of the data is correct or incorrect <br> E. Protect against brute force log-onattempts <br> F. Log unsuccessful and successful attempts <br> G. Raise a security event if a potential attempted or successful breach oflogon controls is detected; <br> H. Display the following information on completion of a successful log-on <br> 1- Date and time of the previous successful log-on <br> 2- Details of any unsuccessful log-on attempts since the last successful log-on <br> I. Not display a password being entered <br> J. Not transmit passwords in clear text over a network <br> K. Terminate inactive sessions after a defined period of inactivity, especially in high risk locations such as public or external areas outside the entity's security management or on mobile devices <br> L. Restrict connection times to provide additional security for high-risk applications and reduce the window of opportunity for unauthorized access |  |  |  |

--- Page 191 ---

Connection time controls should be considered for sensitive computer applications, especially from high risk locations, e.g. public or external areas that are outside the entity's security management. Examples of such restrictions include:
A. Using predetermined time slots, e.g. for batch file transmissions, or regular interactive sessions of short duration
B. Restricting connection times to normal office hours if there is no requirement for overtime or extended-hours operation
C. Considering re-authentication at timed intervals

A time-out facility should clear the session screen and also, possibly later, close both application and network sessions after a defined period of inactivity. The time-out delay should reflect the security risks of the area, the classification of the information being handled and the applications being used, and the risks related to the users of the equipment.

A limited form of time-out facility can be provided for some systems, which clear the screen and prevents unauthorized access but does not close down the application or network sessions.

| T5.5.2 | USER <br> IDENTIFICATION <br> AND <br> AUTHENTICATION | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall create a unique identifier (user ID) for each user and implement a suitable authentication technique.

SUB-CONTROL The entity shall:

1) Provide a unique identifier to each user
2) Enable authentication techniques that are suitable to entity
3) Ensure all restricted activity are logged with the associated authenticated users

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

This control should be applied for all types of users (including technical support personnel, operators, network administrators, system programmers, and database administrators). User IDs should be used to trace activities to the responsible individual. Regular user activities should not be performed from privileged accounts.

In exceptional circumstances, where there is a clear business benefit, the use of a shared user ID for a group of users or a specific job can be used. Approval by management should be documented for such cases. Additional controls may be required to maintain accountability.

Generic IDs for use by an individual should only be allowed either where the functions accessible or actions carried out by the ID do not need to be traced (e.g. read only access), or where there are other controls in place (e.g. password for a generic ID only issued to one staff at a time and logging such instance).

Where strong authentication and identity verification is required, authentication methods alternative to passwords, such as cryptographic means, smart cards, tokens or biometric means, should be used.

--- Page 192 ---

| T5.5.3 | USER CREDENTIALS <br> MANAGEMENT <br> SYSTEM | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
| APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |  |
| CONTROL | The entity shall implement a system for managing user credentials (i.e. <br> passwords). |  |  |
| SUB-CONTROL | The user credential management system shall: <br> 1) Automate the user credential change procedure ensuring the <br> authenticity of the associate user identity <br> 2) Validate that the changed credentials have sufficient strength for <br> their intended use to ensure quality secret authentication <br> 3) Set a maximum lifetime and reuse conditions |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

A management system for user credentials should:
A. Enforce the use of individual user IDs and credentials to maintain accountability
B. Allow users to select and change their own credentials and include a confirmation procedure to allow for input errors
C. Enforce a choice of quality credentials
D. Enforce credential changes
E. Force users to change temporary credentials at the first log-on
F. Maintain a record of previous user credentials and prevent re-use
G. Not display credentials on the screen when being entered
H. Store credential files separately from application system data
I. Store and transmit credentials in protected (e.g. encrypted or hashed-form)

| T5.5.4 | USE OF SYSTEM UTILITIES | PRIORITY | P4 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall restrict and control the use of utility programs that might be capable of overriding system and application controls. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the system utilities and identify the respective appropriate level of protection <br> 2) Keep track of the users access rights provided to the system utilities <br> 3) Restrict use of utility programs only to authorized personnel <br> 4) Monitor the use of utility programs |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

The following guidelines for the use of system utilities should be considered:
A. Use of identification, authentication, and authorization procedures for system utilities
B. Segregation of system utilities from applications software
C. Limitation of the use of system utilities to the minimum practical number of trusted, authorized users
D. Authorization for ad hoc use of systems utilities
E. Limitation of the availability of system utilities, e.g. for the duration of an authorized change
F. Logging of all use of system utilities
G. Defining and documenting of authorization levels for system utilities
H. Removal or disabling of all unnecessary software based utilities and system software
I. Not making system utilities available to users who have access to applications on systems where segregation of duties is required

--- Page 193 ---

| T5.6 | APPLICATION AND INFORMATION ACCESS CONTROL |
| :-- | :-- |
| OBJECTIVE | To prevent unauthorized access to information held in application systems |
| PERFORMANCE <br> INDICATOR | Number of blocked attempts at unauthorized access to applications and <br> information |
| AUTOMATION <br> GUIDANCE | Implement an identity management system and integrate it with existing <br> systems where possible to automate the access restrictions based on the <br> entity policies |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unauthorized access by internal or external user <br> - Backdoor or command and control |


| T5.6.1 | INFORMATION <br> ACCESS <br> RESTRICTION | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall restrict access to information and application system functions in accordance with the access control policy.

SUB-CONTROL
The entity shall:

1) Ensure access to information and application system functions is restricted
2) Ensure access restriction is based on user's roles and responsibilities
3) Assign the appropriate level of access rights to information and application functions
4) For each user and support personnel, adjust their access control based on specific business needs

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Restrictions to access should be based on individual business application requirements. The access control policy should also be consistent with the organizational access policy.

Applying the following guidelines should be considered in order to support access restriction requirements:
A. Providing menus to control access to application system functions
B. Controlling the access rights of users, e.g. read, write, delete, and execute
C. Controlling access rights of other applications
D. Ensuring that outputs from application systems handling sensitive information contain only the information relevant to the use of the output and are sent only to authorized terminals and locations; this should include periodic reviews of such outputs to ensure that redundant information is removed

--- Page 194 ---

| T5.6.2 | SENSITIVE SYSTEM ISOLATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall build a dedicated environment for sensitive systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify sensitive applications and allocate the appropriate resources to ensure its security |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following points should be considered for sensitive system isolation: <br> A. The sensitivity of an application system should be explicitly identified and documented by the application owner <br> B. Access to sensitive systems in data centers should be restricted by using physical cages on workstations to prohibit access to certain external ports, or disabling/removing the ability to insert, read or write to such devices <br> C. When a sensitive application is to run in a shared environment, the application systems with which it will share resources and the corresponding risks should be identified and accepted by the owner of the sensitive application |  |  |  |


| T5.6.3 | PUBLICLY <br> ACCESSIBLE <br> CONTENT | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall not expose nonpublic information to the general public. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop and formalize procedures for the publishing of public <br> information to ensure nonpublic information is not exposed <br> 2) Adopt procedures to periodically verify if sensitive information is <br> exposed to the general public |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| For the publishing of public information, the entity should consider the following: <br> A. Define publishing procedures with required reviews and approvals for any information to be <br> publicly available <br> B. Designate individuals authorized to review and post information onto a publicly accessible <br> information system <br> C. Provide training and awareness sessions for implicated individuals to ensure that publicly <br> accessible information are sanitized from nonpublic information <br> D. Periodically scan publicly accessible information for nonpublic information and correct <br> any inconsistency |  |  |  |

--- Page 195 ---

| T5.7 | MOBILE DEVICES ACCESS CONTROL |
| :--: | :--: |
| OBJECTIVE | To ensure information security when using mobile devices |
| PERFORMANCE INDICATOR | Percentage of mobile computing equipment (e.g. smart phones, laptops, tablets) that are fully compliant with the relevant requirements in the access control policy |
| AUTOMATION GUIDANCE | With asset inventory assembled, many entities use tools to pull information from network assets such as switches and routers regarding the machines connected to the network. Using securely authenticated and encrypted network management protocols, tools can retrieve MAC addresses and other information from network devices that can be reconciled with the entity's asset inventory of servers, workstations, laptops, and other devices. Once MAC addresses are confirmed, switches should implement 802.1x and NAC to only allow authorized systems that are properly configured to connect to the network. <br> Going further, effective entities configure free or commercial network scanning tools to perform network sweeps on a regular basis, sending a variety of different packet types to identify devices connected to the network. Before such scanning can take place, entities should verify that they have adequate bandwidth for such periodic scans by consulting load history and capacities for their networks. In conducting inventory scans, scanning tools could send traditional ping packets (ICMP Echo Request) looking for ping responses to identify a system at a given IP address. Because some systems block inbound ping packets, in addition to traditional pings, scanners can also identify devices on the network using transmission control protocol (TCP) synchronize (SYN) or acknowledge (ACK) packets. Once they have identified IP addresses of devices on the network, some scanners provide robust fingerprinting features to determine the operating system type of the discovered machine. <br> In addition to active scanning tools that sweep the network, other asset identification tools passively listen on network interfaces looking for devices to announce their presence by sending traffic. Such passive tools can be connected to switch span ports at critical places in the network to view all data flowing through such switches, maximizing the chance of identifying systems communicating through those switches. |
| RELEVANT THREATS AND VULNERABILITIES | - Capture data resident on system <br> - Use of stolen login credentials <br> - Remote spying |

--- Page 196 ---

| T5.7.1 | ACCESS CONTROL <br> FOR MOBILE <br> DEVICES | PRIORITY <br> APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall adopt the appropriate security measures to protect against the risks of using portable and mobile devices. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish security measures for usage restrictions, configuration/ connection requirements, and implementation guidance for entitycontrolled mobile devices in line with the access control policy (See T5.1.1) <br> 2) Authorize connection of mobile devices to organizational information systems in accordance with the established security measures |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Usage restrictions and implementation guidance for mobile devices include, for example, configuration management, device identification and authentication, implementation of mandatory protective software (e.g., malicious code detection, firewall), scanning devices for malicious code, updating virus protection software, scanning for critical software updates and patches, conducting primary operating system (and possibly other resident software- integrity checks, and disabling unnecessary hardware (e.g., wireless, infrared). Entities are cautioned that the need to provide adequate security for mobile devices goes beyond the requirements in this control. Many relevant safeguards and countermeasures for mobile devices are reflected in the other security controls in the catalog allocated in the initial control baselines as starting points for the development of security plans and overlays using the tailoring process. |  |  |  |
| The entity should: |  |  |  |
| 1. Prohibit the use of unclassified mobile devices in facilities containing information systems processing, storing, or transmitting classified information unless specifically permitted by the authorizing official (See T2.2.5) |  |  |  |
| 2. Enforce the following restrictions on individuals permitted by the authorizing official to use unclassified mobile devices in facilities containing information systems processing, storing, or transmitting classified information <br> 1- Connection of unclassified mobile devices to classified information systems is prohibited; <br> 2- Connection of unclassified mobile devices to unclassified information systems requires approval from the authorizing official <br> 3- Use of internal or external modems or wireless interfaces within the unclassified mobile devices is prohibited <br> 4- Unclassified mobile devices and the information stored on those devices are subject to random reviews and inspections by the assignment security officials, and if classified information is found, the incident handling policy is followed |  |  |  |
| Also see T1.2.4 on Acceptable use for BYOD |  |  |  |

--- Page 197 ---

| T5.7.2 | TELEWORKING | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall implement security measures to protect information accessed, processed or stored on teleworking sites. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish security measures for using teleworking in line with the access control policy <br> 2) Authorize the usage of teleworking in accordance with the established security measures |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Entities allowing teleworking activities should establish security measures that define the conditions and restrictions for using teleworking. Where deemed applicable and allowed by law, the following matters should be considered: <br> A. The existing physical security of the teleworking site, taking into account the physical security of the building and the local environment <br> B. The proposed physical teleworking environment <br> C. The communications security requirements, taking into account the need for remote access to the entity's internal systems, the sensitivity of the information that will be accessed and pass over the communication link and the sensitivity of the internal system <br> D. The provision of virtual desktop access that prevents processing and storage of information on privately owned equipment <br> E. The threat of unauthorized access to information or resources from other persons using the accommodation, e.g. family and friends <br> F. The use of home networks and requirements or restrictions on the configuration of wireless network services <br> G. Policies and procedures to prevent disputes concerning rights to intellectual property developed on privately owned equipment <br> H. Access to privately owned equipment (to verify the security of the machine or during an investigation), which may be prevented by legislation <br> I. Software licensing agreements that are such that entities may become liable for licensing for client software on workstations owned privately by employees or external party users; <br> J. Anti-virus protection and firewall requirements |  |  |  |
| The guidelines and arrangements to be considered should include <br> A. The provision of suitable equipment and storage furniture for the teleworking activities, where the use of privately owned equipment that is not under the control of the entity is not allowed <br> B. A definition of the work permitted, the hours of work, the classification of information that may be held and the internal systems and services that the teleworker is authorized to access <br> C. The provision of suitable communication equipment, including methods for securing remote access <br> D. Physical security <br> E. Rules and guidance on family and visitor access to equipment and information <br> F. The provision of hardware and software support and maintenance <br> G. The provision of insurance <br> H. The procedures for backup and business continuity <br> I. Audit and security monitoring <br> J. Revocation of authority and access rights, and the return of equipment when the teleworking activities are terminated |  |  |  |  |

--- Page 198 ---

# T6 THIRD-PARTY SECURITY 

| T6 | THIRD PARTY SECURITY |
| :-- | :-- |
| OBJECTIVE | To ensure external stakeholders are compliant with an entities <br> security requirements |
| PERFORMANCE <br> INDICATOR | Frequency of information security incidents involving third parties |


| T6.1 | THIRD PARTY SECURITY POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain a third party security policy covering the security of <br> acquired services |
| PERFORMANCE <br> INDICATOR | Extent of third party security policy deployment and adoption across <br> the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable third party security policy <br> - Unawareness of third party security policy among IT staff |

--- Page 199 ---

| T6.1.1 | THIRD PARTY SECURITY POLICY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall establish a third party security policy to facilitate the implementation of the associated controls. |  |  |  |
| SUB-CONTROL | The third party security policy shall: <br> 1) Be appropriate to the relationship of the entity and the third party <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline the roles and responsibilities for managing third party <br> 4) Provide the framework for setting information security objectives and/or include information security objectives to be used when engaging third parties <br> 5) Be documented and communicated to the third party <br> 6) Be read and acknowledged formally by the third party <br> 7) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The third party security policy facilitates the implementation of the associated controls to safeguard the entity's information assets when third parties are involved in their operation. The policy can, for example, contain in addition to the required sub-controls: <br> A. Third party engagement terms and conditions <br> B. Information security requirements <br> C. Audit requirements |  |  |  |  |
| The third party security policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |  |

--- Page 200 ---

|  T6.2 | THIRD PARTY SERVICE DELIVERY MANAGEMENT  |
| --- | --- |
|  OBJECTIVE | To ensure third parties implement and maintain the appropriate level of information security and service delivery  |
|  PERFORMANCE INDICATOR | Frequency of information security incidents involving third parties  |
|  AUTOMATION GUIDANCE | Not applicable  |
|  RELEVANT THREATS AND VULNERABILITIES | - Abuse of functionality
- Data from untrustworthy sources  |

|  T6.2.1 | SERVICE DELIVERY | PRIORITY | P2  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT  |
|  CONTROL | The entity shall monitor third party service delivery. |  |   |
|  SUB-CONTROL | The entity shall:
1) Ensure that security requirements for third parties are included in the service delivery agreement for each party
2) Ensure these security requirements are measurable
3) Require third parties to measure and report to the entity on these service requirements |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  Service delivery by a third party should include the agreed security arrangements, service definitions, and aspects of service management. In case of outsourcing arrangements, the entity should plan the necessary transitions (of information, information systems, and anything else that needs to be moved), and should ensure that security is maintained throughout the transition period. |  |  |   |
|  The entity should ensure that the third party maintains sufficient service capability together with workable plans designed to ensure that agreed service continuity levels are maintained following major service failures or disaster. |  |  |   |

--- Page 201 ---

| T6.2.2 | MONITORING AND REVIEW OF THIRD PARTY SERVICES | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall monitor and review the services, reports and records provided by the third party. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) monitor third parties' services and ensure required delivery reports are received <br> 2) ensure reports received from third parties are reviewed by qualified personnel <br> 3) ensure that information security incidents and problems identified in the reports are managed properly <br> 4) carry out audits for third parties services at a regular basis |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Monitoring and review of third party services should involve a service management relationship and process between the entity and the third party to: <br> A. Monitor service performance levels to check adherence to the agreements; <br> B. Review service reports produced by the third party and arrange regular progress meetings as required by the agreements; <br> C. Provide information about information security incidents and review of this information by the third party and the entity as required by the agreements and any supporting guidelines and procedures; <br> D. Review third party audit trails and records of security events, operational problems, failures, tracing of faults and disruptions related to the service delivered; <br> E. Resolve and manage any identified problems. |  |  |  |
| The responsibility for managing the relationship with a third party should be assigned to a designated individual or service management team. In addition, the entity should ensure that the third party assigns responsibilities for checking for compliance and enforcing the requirements of the agreements. Sufficient technical skills and resources should be made available to monitor the requirements of the agreement, in particular the information security requirements, are being met. Appropriate action should be taken when deficiencies in the service delivery are observed. |  |  |  |
| The entity should maintain sufficient overall control and visibility into all security aspects for sensitive or critical information or information systems accessed, processed or managed by a third party. The entity should ensure they retain visibility into security activities such as change management, identification of vulnerabilities, and information security incident reporting/response through a clearly defined reporting process, format and structure |  |  |  |

--- Page 202 ---

| T6.2.3 | MANAGING | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  | CHANGES TO THIRD | APPLICABILITY | BASED ON RISK |
|  | PARTY SERVICES |  | ASSESSMENT |
| CONTROL | The entity shall manage changes to the provision of third party services, including maintaining and improving existing information security policies, procedures and controls. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Ensure that third party service agreements include a methodology for communicating change management issues between the entity and the third party <br> 2) Define the parameters for changes that must be communicated between the entity and the third party <br> 3) Assess the changes taking into account the criticality of business systems and processes involved and re-assessment of risks |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The process of managing changes to a third party service needs to take account of: <br> A. Changes made by the entity to implement: <br> 1- Enhancements to the current services offered <br> 2- Development of any new applications and systems <br> 3- Modifications or updates of the entity's policies and procedures <br> 4- New controls to resolve information security incidents and to improve security <br> B. Changes in third party services to implement: <br> 1- Changes and enhancement to networks <br> 2- Use of new technologies <br> 3- Adoption of new products or newer versions/releases <br> 4- New development tools and environments <br> 5- Changes to physical location of service facilities <br> 6- Change of vendors |  |  |  |

--- Page 203 ---

| T6.3 | CLOUD COMPUTING |
| :-- | :-- |
| OBJECTIVE | To secure information stored, processed, and retrieved through cloud <br> services |
| PERFORMANCE <br> INDICATOR | Percentage of service level agreements capturing all relevant cloud <br> security requirements |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Abuse of functionality <br> - Accidental leaks / sharing of data <br> - Illegal processing of data |

--- Page 204 ---

| T6.3.1 | INFORMATION SECURITY REQUIREMENTS FOR CLOUD ENVIRONMENTS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall define information security requirements covering the retention, processing, and storage of data in cloud environments. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Perform necessary due diligence to determine requirements and restrictions relevant to information processing, storage and retention in the cloud environment <br> 2) Include the cloud environment (and, where possible, its components) into the risk assessment process <br> 3) Develop and maintain information governance policies and procedures to ensure compliance with identified requirements and risk mitigation strategies <br> 4) Ensure information about security incidents that happen at the cloud service provider are communicated <br> 5) Where possible, reserve a right to audit the security arrangements in place at cloud service provider |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |
| A risk-based approach used to establish data security requirements for cloud environments should consider the following: <br> A. Regulatory and other requirements potentially limiting the processing, storage and retention of information in external entities, for example laws or business agreements preventing certain types of information from being stored outside national borders, privacy legislation, and / or regulatory, statutory, contractual, business, and other requirements <br> B. The complete life cycle of information across entire networks, including both within cloud and non-cloud elements, as well as the interchange of information between these two elements <br> C. Awareness of where sensitive information is stored and transmitted across applications, databases, servers and network infrastructure <br> D. Compliance with defined retention periods and end-of-life disposal requirements <br> E. Information classification and protection from unauthorized use, access, loss, destruction, and falsification <br> F. Balancing the expected benefits of leveraging cloud-based services against the potential risks |  |  |  |

--- Page 205 ---

| T6.3.2 | SERVICE DELIVERY <br> AGREEMENTS WITH <br> CLOUD PROVIDERS | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall document relevant security requirements in service delivery agreements with cloud service providers. |  |  |
| SUB-CONTROL | Each service delivery agreement for cloud services shall include provisions for: <br> 1) Understanding and maintaining awareness of where information with applicable restrictions will be stored or transmitted in the cloud environment <br> 2) Ensuring appropriate information migration plans at the end of the service period <br> 3) Ensuring all other cloud security requirements determined relevant by the entity are included in the service delivery agreement |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| When establishing service delivery agreement for cloud-based services, it is the entity's responsibility to define security requirements for the cloud vendor. This should also take into consideration that the entity may have different levels of ability to negotiate these terms with a vendor based on the type of cloud services being purchased (e.g. private vs. public). <br> Part of the entity's responsibility includes understanding, where possible, where information will be stored, processed, or transmitted to ensure that often sensitive information privacy laws and other legal restrictions (e.g. prohibiting transmission of certain types of information outside national borders) are respected. <br> In addition, the entity should ensure that the terms and conditions of service delivery agreements provide ample clarification on how information will be migrated from the selected cloud service provider to another provider (or back to the entity) at the termination of the service delivery agreement. This is critical to ensuring that the entity is not "held hostage" by the service provider. |  |  |  |

--- Page 206 ---

# T7 INFORMATION SYSTEMS ACQUISITION, DEVELOPMENT AND MAINTENANCE

|  T7 | INFORMATION SYSTEMS ACQUISITION, DEVELOPMENT AND MAINTENANCE  |
| --- | --- |
|  OBJECTIVE | To prevent information misuse or unauthorized modification and to elevate security levels in applications, during development as well as to manage technical vulnerabilities.  |
|  PERFORMANCE INDICATOR | Percentage of information systems compliant to information systems acquisition, development and maintenance policy.  |
|  T7.1 | INFORMATION SYSTEMS ACQUISITION, DEVELOPMENT AND MAINTENANCE POLICY  |
|  OBJECTIVE | To maintain an information systems acquisition, development and maintenance policy covering the security of information systems throughout its lifecycle.  |
|  PERFORMANCE INDICATOR | Extent of information systems acquisition, development and maintenance policy deployment and adoption across the entity  |
|  AUTOMATION GUIDANCE | Not applicable  |
|  RELEVANT THREATS AND VULNERABILITIES | - Unsuitable information systems acquisition, development and maintenance policy
- Partial information systems acquisition, development and maintenance policy not covering the entire asset lifecycle  |

--- Page 207 ---

| T7.1.1 | INFORMATION <br> SYSTEMS <br> ACQUISITION, <br> DEVELOPMENT AND <br> MAINTENANCE POLICY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall establish an information systems acquisition, development, and maintenance policy. |  |  |  |
| SUB-CONTROL | The information systems acquisition, development, and maintenance policy shall: <br> 1) Be appropriate to the relationship of the entity and all internal and external parties involved in the process <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline the roles and responsibilities <br> 4) Provide the framework for setting information security objectives and/ or include information security objectives to be used when engaging in the process <br> 5) Be documented and communicated to all users <br> 6) Be read and acknowledged formally by all users <br> 7) Be maintained, reviewed and updated at planned intervals or if significant changes occur |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The information systems acquisition, development and maintenance policy facilitates the implementation of the associated controls to integrate information security requirements into the software life cycle of information systems that contain protected data. The policy can, for example, contain in addition to the required sub-controls: <br> A. Information security requirements around systems specification, correct processing, cryptography, system files, etc. <br> B. Audit requirements |  |  |  |  |
| The information systems acquisition, development and maintenance policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |  |


| T7.2 | SECURITY REQUIREMENTS OF INFORMATION SYSTEMS |
| :-- | :-- |
| OBJECTIVE | To ensure that security requirements are established and functionally <br> integrated into information systems |
| PERFORMANCE <br> INDICATOR | Percentage of systems implementations accepted into service with all <br> security requirements implemented |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Equipment malfunction <br> - Abuse of functionality |

--- Page 208 ---

| T7.2.1 | SECURITY <br> REQUIREMENTS <br> ANALYSIS AND <br> SPECIFICATION | PRIORITY |  |
| :-- | :-- | :-- | :-- | :-- |

# P3 

## APPLICABILITY

BASED ON RISK ASSESSMENT

CONTROL
The entity shall develop information security requirements for new information systems or enhancements to existing information systems.

SUB-CONTROL
The security requirements shall:

1) Be used for new information systems or enhancements to existing information systems
2) Be approved by the appropriate business manager or equivalent
3) Address all requirements for security controls identified during the risk assessment
4) Outline how to verify that the requirements for security controls have been met
5) Be included in the statement of business and technical requirements

## IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY)

Information security requirements should be identified using various methods such as regulations and policies, reviews threat modeling and vulnerability thresholds/vulnerably remediation. Results from the identification should be documented merging views of all stakeholders.

Security requirements and controls should reflect the business value of the information involved and the potential negative business impact which might result from lack of adequate security.

System requirements for information security and processes for implementing security should be integrated in the early stages of information system projects. Controls introduced at the design stage are significantly cheaper to implement and maintain than those included during or after implementation.

The sizing of information systems should take into account enabling all security features in that system; i.e. higher specifications model of Security-Systems so that when security features are enabled they do not cause slow-down and degradation in the information systems performance.

For applications systems providing services or transferring information over public networks, the system requirements should also consider the following:
A. The level of confidence each party requires in each other's claimed identity, e.g. through authentication
B. Authorization processes associated with who may approve contents of, issuing or signing key transactional documents
C. Ensuring that communicating partners are fully informed of their authorizations for provision or use of the service
D. Determining and meeting requirements for confidentiality, integrity, proof of dispatch and receipt of key documents and the non-repudiation of contracts, e.g. associated with tendering and contract processes
E. The level of trust required in the integrity of key documents
F. The confidentiality of any confidential information
G. The confidentiality and integrity of any order transactions, payment information, delivery address details and confirmation of receipts
H. The degree of verification appropriate to verify payment information supplied by a customer
I. Selecting the most appropriate settlement form of payment to guard against fraud

--- Page 209 ---

J. The level of protection required to maintain the confidentiality and integrity of order information;
K. Avoidance of loss or duplication of transaction information;
L. Liability associated with any fraudulent transactions;
M. Insurance requirements;
N. Transaction related requirements such as authenticity, confidentiality and integrity of transaction related data, non-repudiation and protection of any transaction related data.

If products are acquired, a formal testing and acquisition process should be followed. Contracts with the supplier should address the identified security requirements. Where the security functionality in a proposed product does not satisfy the specified requirement then the risk introduced and associated controls should be reconsidered prior to purchasing the product.

Available guidance for security configuration of the product aligned with the final software / service stack of that system should be evaluated and implemented.

Criteria for accepting products should be defined e.g., in terms of their functionality, which give assurance that the identified security requirements are met. Products should be evaluated against these criteria before acquisition. Where additional functionality is supplied and causes a security risk, this should be disabled or the proposed control structure should be reviewed to determine if advantage can be taken of the enhanced functionality available.

| T7.2.2 | DEVELOPER-PROVIDED TRAINING | PRIORITY | BASED ON RISK ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall require the developer of the information system, system component, or information system service to provide the trainings needed. |  |  |
| SUB-CONTROL | The entity shall require the developer to: <br> 1) Identify training requirements based on implemented security functions and in line with the Awareness and Training Policy (refer to M3.1.1) for the correct use and operation of the functions <br> 2) Design and execute appropriate training programs to meet these requirements <br> 3) Include training provisions in the relevant service delivery agreement |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| This control applies to external and internal (in-house- developers). Training of personnel is an essential element to ensure the effectiveness of security controls implemented within organizational information systems. Training options include, for example, classroom-style training, web-based/ computer-based training, and hands-on training. Entities can also request sufficient training materials from developers to conduct in-house training or offer self-training to organizational personnel. Entities determine the type of training necessary and may require different types of training for different security functions, controls, or mechanisms. |  |  |  |

--- Page 210 ---

| T7.3 | CORRECT PROCESSING IN APPLICATIONS |
| :--: | :--: |
| OBJECTIVE | To prevent errors, loss, unauthorized modification or misuse of information in applications |
| PERFORMANCE INDICATOR | Percentage of systems for which data validation controls have been adequately defined, implemented, and proven effective by thorough testing |
| AUTOMATION GUIDANCE | Source code testing tools, web application security scanning tools, and object code testing tools have proven useful in securing application software, along with manual application security penetration testing by testers who have extensive programming knowledge and application penetration testing expertise. The Common Weakness Enumeration (CWE) initiative is used by many such tools to identify the weaknesses that they find. Entities can also use CWE to determine which types of weaknesses they are most interested in addressing and removing. When evaluating the effectiveness of testing for these weaknesses, MITRE's Common Attack Pattern Enumeration and Classification can be used to organize and record the breadth of the testing for the CWEs and to enable testers to think like attackers in their development of test cases. |
| RELEVANT THREATS AND VULNERABILITIES | - Software malfunction <br> - Illegal processing of data <br> - Injection flaws, such as SQL, OS, and LDAP <br> - Broken Authentication and Session Management <br> - Cross-Site Scripting (XSS) |

--- Page 211 ---

| T7.3.1 | INPUT DATA <br> VALIDATION | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall validate data input to applications to ensure that this data is correct and appropriate. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a set of guidelines or parameters to be used to validate data input into applications <br> 2) Define a set of values for each guideline or parameter to identify acceptable and unacceptable values <br> 3) Provide guidance on how to validate each guideline or parameter |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Checks should be applied to the input of business transactions, standing data (e.g. names and addresses, credit limits, customer reference numbers), and parameter tables (e.g. sales prices, currency conversion rates, tax rates). The following guidelines should be considered: <br> A. Dual input or other input checks, such as boundary checking or limiting fields to specific ranges of input data, to detect the following errors: <br> 1- Out-of-range values <br> 2- Invalid characters in data fields <br> 3- Missing or incomplete data <br> 4- Exceeding upper and lower data volume limits <br> 5- Unauthorized or inconsistent control data <br> B. Periodic review of the content of key fields or data files to confirm their validity and integrity <br> C. Inspecting hard-copy input documents for any unauthorized changes (all changes to input documents should be authorized) <br> D. Procedures for responding to validation errors <br> E. Procedures for testing the plausibility of the input data <br> F. Defining the responsibilities of all personnel involved in the data input process <br> G. Creating a log of the activities involved in the data input process |  |  |  |

--- Page 212 ---

| T7.3.2 | CONTROL OF <br> INTERNAL <br> PROCESSING | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall incorporate validation checks into applications to detect any corruption of information through processing errors or deliberate acts. |  |  |
|  | The entity shall: <br> 1) Provide guidelines to application developers on minimum requirements for validation checks for applications under development <br> 2) Require application developers to provide evidence of compliance with minimum requirements <br> 3) Periodically review existing applications to ensure validation checks included during their development still met minimum requirements |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The design and implementation of applications should ensure that the risks of processing failures leading to a loss of integrity are minimized. Specific areas to consider include: <br> A. The use of add, modify, and delete functions to implement changes to data <br> B. The procedures to prevent programs running in the wrong order or running after failure of prior processing <br> C. The use of appropriate programs to recover from failures to ensure the correct processing of data <br> D. Protection against attacks using buffer overruns/overflows |  |  |  |
| An appropriate checklist should be prepared, activities documented, and the results should be kept secure. Examples of checks that can be incorporated include the following: <br> A. Session or batch controls, to reconcile data file balances after transaction updates <br> B. Balancing controls, to check opening balances against previous closing balances, namely <br> 1- Run-to-run controls <br> 2- File update totals <br> 3- Program-to-program controls <br> C. Validation of system-generated input data <br> D. Checks on the integrity, authenticity or any other security feature of data or software downloaded, or uploaded, between central and remote computers <br> E. Hash totals of records and files <br> F. Checks to ensure that application programs are run at the correct time <br> G. Checks to ensure that programs are run in the correct order and terminate in case of a failure, and that further processing is halted until the problem is resolved <br> H. Creating a log of the activities involved in the processing |  |  |  |

--- Page 213 ---

| T7.3.3 | MESSAGEINTEGRITY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall ensure authenticity and integrity of messages in applications. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) identify requirements to ensure authenticity and integrity of messages transmitted between systems and applications <br> 2) adopt proper controls to address the identified requirements |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| An assessment of security risks should be carried out to determine if message integrity is required and to identify the most appropriate method of implementation. Proper technical countermeasures (as hashing/digital signature)should be adopted to ensure integrity of messages during their transmission |  |  |  |


| T7.3.4 | OUTPUT DATA <br> VALIDATION | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall validate data output from an application |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define output validation procedures to ensure that the processing of <br> stored information is correct and appropriate to the circumstances |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Output validation may include: |  |  |  |
| A. Plausibility checks to test whether the output data is reasonable |  |  |  |
| B. Reconciliation control counts to ensure processing of all data |  |  |  |
| C. Providing sufficient information for a reader or subsequent processing system to determine <br> the accuracy, completeness, precision, and classification of the information |  |  |  |
| D. Procedures for responding to output validation tests |  |  |  |
| E. Defining the responsibilities of all personnel involved in the data output process |  |  |  |
| F. Creating a log of activities in the data output validation process |  |  |  |

--- Page 214 ---

| T7.4 | CRYPTOGRAPHIC CONTROLS |
| :-- | :-- |
| OBJECTIVE | To protect the confidentiality, authenticity or integrity of information by <br> cryptographic means. |
| PERFORMANCE <br> INDICATOR | Percentage of systems containing valuable/sensitive data for which <br> suitable cryptographic controls have been fully implemented |
| AUTOMATION <br> GUIDANCE | Cryptography can only be performed through the use of automated <br> cryptographic systems. These systems should automate all processes, <br> including key generation, distribution, revocation, restoration, etc. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Weak cryptography used for sensitive data <br> - Eavesdropping / Packet sniffing Sensitive Data Exposure |


| T7.4.1 | POLICY ON THE USE <br> OF CRYPTOGRAPHIC <br> CONTROLS | PRIORITY <br> APPLICABILITY | P2 |
| :-- | :-- | :-- | :-- |
| CONTROL | The entity shall establish a policy on the use of cryptographic controls |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop and document a policy for the use of cryptographic controls <br> in line with the criticality of the information to be protected <br> 2) Ensure the policy takes into account the sector or national level <br> restrictions including NESA's relevant issuances and guidance in <br> this regard <br> 3) Share the policy with relevant users <br> 4) Review and update the policy at planned intervals or if significant <br> changes occur | BASED ON RISK <br> ASSESSMENT |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |

--- Page 215 ---

When developing a cryptographic policy the following should be considered:
A. The management approach towards the use of cryptographic controls across the entity, including the general principles under which business information should be protected
B. based on a risk assessment, the required level of protection should be identified taking into account the type, strength, and quality of the encryption algorithm required
C. The use of encryption for protection of sensitive information transported by mobile or removable media, devices or across communication lines
D. The approach to key management, including methods to deal with the protection of cryptographic keys and the recovery of encrypted information in the case of lost, compromised or damaged keys
E. Roles and responsibilities, e.g. who is responsible for:

1- The implementation of the policy
2- The key management, including key generation
F. These Standards to be adopted for the effective implementation throughout the entity (which solution is used for which business processes)
G. The impact of using encrypted information on controls that rely upon content inspection (e.g. virus detection)
H. Any other NESA's relevant issuances, guidance, and activities in this regard

When implementing the entity's cryptographic policy, consideration should be given to the regulations and national restrictions that might apply to the use of cryptographic techniques in different parts of the world and to the issues of trans-border flow of encrypted information.
Cryptographic controls can be used to achieve different security objectives, e.g.:
CONFIDENTIALITY: using encryption of information to protect sensitive or critical information, either stored or transmitted
INTEGRITY/AUTHENTICITY: using digital signatures or message authentication codes to protect the authenticity and integrity of stored or transmitted sensitive or critical information
NON-REPUDIATION: using cryptographic techniques to obtain proof of the occurrence or nonoccurrence of an event or action

Cryptographic techniques can also be used to implement the dissemination rules of information sharing, e.g. through information rights management.

--- Page 216 ---

| T7.4.2 | KEY MANAGEMENT | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall establish key management to support the entity's use of cryptographic techniques. |  |  |
|  | The entity shall: <br> 1) Develop a key management policy and process to control the generation of keys taking into account NESA's issuances with regard to key management <br> 2) Define key storing standards <br> 3) Define procedures to revoke/block keys and to repair damage or corrupted keys <br> 4) Protect all cryptographic keys against modification and loss <br> 5) Protect secret and private keys against unauthorized use and disclosure |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| All cryptographic keys should be protected against modification, loss, and destruction. In addition, secret and private keys need protection against unauthorized disclosure. Equipment used to generate, store and archive keys should be physically protected. <br> A key management system should be based on an agreed set of standards, procedures, and secure methods for: <br> A. Generating keys for different cryptographic systems and different applications <br> B. Generating and obtaining public key certificates <br> C. Distributing keys to intended users, including how keys should be activated when received <br> d. Storing keys, including how authorized users obtain access to keys <br> E. Changing or updating keys including rules on when keys should be changed and how this will be done <br> F. Dealing with compromised keys <br> G. Revoking keys including how keys should be withdrawn or deactivated, e.g. when keys have been compromised or when a user leaves an entity (in which case keys should also be archived) <br> H. Recovering keys that are lost or corrupted as part of business continuity management, e.g. for recovery of encrypted information <br> I. Archiving keys, e.g. for information archived or backed up <br> J. Destroying keys <br> K. Logging and auditing of key management related activities |  |  |
| In order to reduce the likelihood of compromise, activation, and deactivation dates for keys should be defined so that the keys can only be used for a limited period of time. This period of time should be dependent on the circumstances under which the cryptographic control is being used, and the perceived risk. <br> In addition to securely managing secret and private keys, the authenticity of public keys should also be considered. This authentication process can be done using public key certificates which are normally issued by a certification authority, which should be a recognized entity with suitable controls and procedures in place to provide the required degree of trust. <br> The contents of service level agreements or contracts with external suppliers of cryptographic services, e.g. with a certification authority, should cover issues of liability, reliability of services and response times for the provision of services. |  |  |  |

--- Page 217 ---

| T7.5 | SECURITY OF SYSTEM FILES |
| :-- | :-- |
| OBJECTIVE | To ensure the security of system files |
| PERFORMANCE <br> INDICATOR | Percentage of systems assessed as fully compliant with the information <br> systems acquisition, development and maintenance policy |
| AUTOMATION <br> GUIDANCE | Security of system files can only be achieved through the use of automated <br> controls, including but not limited to file permission restrictions, file access <br> log, and file hashing for integrity check. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unauthorized access to system files <br> - Corruption of data |


| T7.5.1 | CONTROL OF <br> OPERATIONAL <br> SOFTWARE | PRIORITY <br> APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall control the installation of software on operational systems. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Allow the installation of software only by authorized administrators <br> 2) Inhibit installation of software by users, unless justified by their role/ business need <br> 3) Keep an original copy of every installed software, including previous versions <br> 4) Have a rollback strategy <br> 5) Have an audit log of all software installations |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| To minimize the risk of corruption to operational systems, the following guidelines should be considered to control changes: <br> A. The updating of the operational software, applications, and program libraries should only be performed by trained administrators upon appropriate management authorization <br> B. Operational systems should only hold approved executable code, and not development code or compilers <br> C. Applications and operating system software should only be implemented after extensive and successful testing; the tests should include tests on usability, security, effects on other systems and user-friendliness, and should be carried out on separate systems; it should be ensured that all corresponding program source libraries have been updated <br> D. A configuration control system should be used to keep control of all implemented software as well as the system documentation <br> E. A rollback strategy should be in place before changes are implemented <br> F. An audit log should be maintained of all updates to operational program libraries <br> G. Previous versions of application software should be retained as a contingency measure <br> H. Old versions of software should be archived, together with all required information and parameters, procedures, configuration details, and supporting software for as long as the data is retained in archive |  |  |  |

--- Page 218 ---

Vendor supplied software used in operational systems should be maintained at a level supported by the supplier. Over time, software vendors will cease to support older versions of software. The entity should consider the risks of relying on unsupported software.

Any decision to upgrade to a new release should take into account the business requirements for the change, and the security of the release, i.e. the introduction of new security functionality or the number and severity of security problems affecting this version. Software patches should be applied when they can help to remove or reduce security weaknesses.

Physical or logical access should only be given to suppliers for support purposes when necessary, and with management approval. The supplier's activities should be monitored. Computer software may rely on externally supplied software and modules, which should be monitored and controlled to avoid unauthorized changes, which could introduce security weaknesses.

| T7.5.2 | PROTECTION OF SYSTEM TEST DATA | PRIORITY | P3 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall ensure the protection of system test data. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Use sample data sets to test data applications <br> 2) Limit the transfer of real data from production environment to the test environment, and to be done only after the appropriate authorization <br> 3) Erase any data from test applications immediately after testing is completed <br> 4) Keep track of any copy/erase of data between production and testing environment |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The use of operational databases containing personal information or any other sensitive information for testing purposes should be avoided. If personal or otherwise sensitive information is used for testing purposes, all sensitive details and content should be removed or modified beyond recognition before use. The following guidelines should be applied to protect operational data, when used for testing purposes: <br> A. The access control procedures, which apply to operational application systems, should also apply to test application systems <br> B. There should be separate authorization each time operational information is copied to a test application system <br> C. Operational information should be erased from a test application system immediately after the testing is complete <br> D. The copying and use of operational information should be logged to provide an audit trail |  |  |  |

--- Page 219 ---

| T7.5.3 | ACCESS CONTROL <br> TO PROGRAM <br> SOURCE CODE | PRIORITY <br> APPLICABILITY | P3 <br> BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall restrict the access to program source code. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define an access control policy to source code <br> 2) Define and periodically review permissions <br> 3) Keep an audit log of all accesses |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Access to program source code and associated items (such as designs, specifications, verification plans and validation plans) should be strictly controlled, in order to prevent the introduction of unauthorized functionality and to avoid unintentional changes. For program source code, this can be achieved by controlled central storage of such code, preferably in program source libraries. The following guidelines should then be considered to control access to such program source libraries in order to reduce the potential for corruption of computer programs: <br> A. Where possible, program source libraries should not be held in operational systems <br> B. The program source code and the program source libraries should be managed according to established procedures <br> C. Support personnel should not have unrestricted access to program source libraries <br> D. The updating of program source libraries and associated items, and the issuing of program sources to programmers should only be performed after appropriate authorization has been received <br> E. Program listings should be held in a secure environment <br> F. An audit log should be maintained of all accesses to program source libraries <br> G. Maintenance and copying of program source libraries should be subject to strict change control procedures |  |  |  |


| T7.6 | SECURITY IN DEVELOPMENT AND SUPPORT PROCESSES |
| :-- | :-- |
| OBJECTIVE | To maintain the security of application system software and information |
| PERFORMANCE <br> INDICATOR | Number of cases where the change management processes have not <br> been executed correctly |
| AUTOMATION <br> GUIDANCE | Entity should adopt technical solutions to monitor application and program <br> changes/updates |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable security for development and support processes <br> - Lack of proper technical review of applications after operating <br> system changes <br> - Leakage of information |

--- Page 220 ---

| T7.6.1 | CHANGE CONTROL PROCEDURES | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall control the implementation of changes by the use of formal change control procedures. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop a change control procedure <br> 2) Keep track record of all changes <br> 3) Keep a copy of every version of the software, adopting appropriate integrity verification procedures <br> 4) Ensure all relevant documentations are up-to-date <br> 5) Ensure proper planning to perform changes implementation at the right time |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Formal change control procedures should be documented and enforced in order to minimize the corruption of information systems. Introduction of new systems and major changes to existing systems should follow a formal process of documentation, specification, testing, quality control, and managed implementation. |  |  |  |  |
| This process should include a risk assessment, analysis of the impacts of changes, and specification of security controls needed. This process should also ensure that existing security and control procedures are not compromised, that support programmers are given access only to those parts of the system necessary for their work, and that formal agreement and approval for any change is obtained. |  |  |  |  |
| Wherever practicable, application and operational change control procedures should be integrated. The change procedures should include: <br> A. Maintaining a record of agreed authorization levels <br> B. Ensuring changes are submitted by authorized users <br> C. Reviewing controls and integrity procedures to ensure that they will not be compromised by the changes <br> D. Identifying all software, information, database entities, and hardware that require amendment <br> E. Obtaining formal approval for detailed proposals before work commences <br> F. Ensuring authorized users accept changes prior to implementation <br> G. Ensuring that the system documentation set is updated on the completion of each change and that old documentation is archived or disposed of <br> H. Maintaining a version control for all software updates <br> I. Maintaining an audit trail of all change requests <br> J. Ensuring that operating documentation and user procedures are changed as necessary to remain appropriate <br> K. Ensuring that the implementation of changes takes place at the right time and does not disturb the business processes involved |  |  |  |  |

--- Page 221 ---

|  T7.6.2 | TECHNICAL REVIEW OF APPLICATIONS AFTER OPERATING SYSTEM CHANGES | PRIORITY | P3  |
| --- | --- | --- | --- |
|   |  | APPLICABILITY | BASED ON RISK ASSESSMENT  |
|  CONTROL | The entity shall review and test business critical applications after changes in the operating systems. |  |   |
|  SUB-CONTROL | The entity shall:
1) Test any application in a testing environment when operating systems are changed (including patches and configurations)
2) Monitor operating system and application logs for any anomaly
3) Always define a rollback procedure
4) Ensure that changes are reflected in any asset database and in any technical contingency plan |  |   |
|  IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |   |
|  This process should cover:
A. Review of application control and integrity procedures to ensure that they have not been compromised by the operating system changes
B. Ensuring that the annual support plan and budget will cover reviews and system testing resulting from operating system changes
C. Ensuring that notification of operating system changes is provided in time to allow appropriate tests and reviews to take place before implementation
D. Ensuring that appropriate changes are made to the business continuity plans
A specific group or individual should be given responsibility for monitoring vulnerabilities and vendors' releases of patches and fixes. |  |  |   |

--- Page 222 ---

| T7.6.3 | RESTRICTIONS <br> ON CHANGES <br> TO SOFTWARE <br> PACKAGES | PRIORITY | P2 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |

CONTROL The entity shall restrict the changes to software packages.

SUB-CONTROL
The entity shall:

1) Define who is entitled to approve changes to software/applications
2) Test any change in a testing environment before moving it to production environment
3) In case of major changes in critical software and applications, perform a Secure Code Review

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

As far as possible, and practicable, vendor-supplied software packages should be used without modification. Where a software package needs to be modified the following points should be considered:
A. The risk of built-in controls and integrity processes being compromised
B. Whether the consent of the vendor should be obtained
C. The possibility of obtaining the required changes from the vendor as standard program updates
D. The impact if the entity becomes responsible for the future maintenance of the software as a result of changes

If changes are necessary the original software should be retained and the changes applied to a clearly identified copy. A software update management process should be implemented to ensure the most up-to-date approved patches and application updates are installed for all authorized software. All changes should be fully tested and documented, so that they can be reapplied if necessary to future software upgrades. If required, the modifications should be tested and validated by an independent evaluation body.

--- Page 223 ---

| T7.6.4 | INFORMATION <br> LEAKAGE | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall prevent opportunities for information leakage. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Adopt Data Leak Prevention (DLP) measures <br> 2) Adopt identity and access management solutions to limit access to critical data only to authorized personnel <br> 3) Define and enforce a data/information classification policy |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| The following should be considered to limit the risk of information leakage, e.g. through the use and exploitation of covert channels: <br> A. Scanning of outbound media and communications for hidden information <br> B. Masking and modulating system and communications behavior to reduce the likelihood of a third party being able to deduce information from such behavior <br> C. Making use of systems and software that are considered to be of high integrity, e.g. using evaluated products <br> D. Regular monitoring of personnel and system activities, where permitted under existing legislation or regulation <br> E. Monitoring resource usage in computer systems |  |  |  |


| T7.6.5 | OUTSOURCED <br> SOFTWARE <br> DEVELOPMENT | PRIORITY | P3 |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall supervise outsourced software development. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a secure coding policy <br> 2) Define a Quality Assurance (QA) process <br> 3) Include in the software acquisition contract a clause to oblige third <br> part to be compliant to Entity secure coding policy, to align to Entity <br> QA process; contract shall also include the possibility to conduct audit <br> on the third party <br> 4) Specify in the software development contract any requirement and <br> information security functionality <br> 5) Conduct a source code review to identify potential vulnerabilities <br> and/or malicious code or code that does not conform to the <br> functionalities required |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Where software development is outsourced, the following points should be considered: <br> A. Licensing arrangements, code ownership, and intellectual property rights <br> B. Certification of the quality and accuracy of the work carried out <br> C. Escrow arrangements in the event of failure of the third party <br> D. Rights of access for audit of the quality and accuracy of work done <br> E. Contractual requirements for quality and security functionality of code <br> F. Testing before installation to detect malicious and Trojan code |  |  |  |

--- Page 224 ---

| T7.7 | TECHNICAL VULNERABILITY MANAGEMENT |
| :--: | :--: |
| OBJECTIVE | To reduce risks resulting from exploitation of published or identified technical vulnerabilities |
| PERFORMANCE INDICATOR | Percentage of identified vulnerabilities mitigated within the acceptable time periods as defined in security requirements |
| AUTOMATION GUIDANCE | A large number of vulnerability scanning tools are available to evaluate the security configuration of systems. Some entities have also found commercial services using remotely managed scanning appliances to be effective. To help standardize the definitions of discovered vulnerabilities in multiple departments of an entity or even across entities it is preferable to use vulnerability scanning tools that measure security flaws and map them to vulnerabilities and issues categorized using one or more of the following industry-recognized vulnerability, configuration, and platform classification schemes and languages: CVE, CCE, OVAL, CPE, CVSS, and/or XCCDF. <br> Advanced vulnerability scanning tools can be configured with user credentials to log in to scanned systems and perform more comprehensive scans than can be achieved without login credentials. The frequency of scanning activities, however, should increase as the diversity of an entity's systems increases to account for the varying patch cycles of each vendor. <br> In addition to the scanning tools that check for vulnerabilities and misconfigurations across the network, various free and commercial tools can evaluate security settings and configurations of local machines on which they are installed. Such tools can provide fine-grained insight into unauthorized changes in configuration or the inadvertent introduction of security weaknesses by administrators. <br> Effective entities link their vulnerability scanners with problem-ticketing systems that automatically monitor and report progress on fixing problems, and that make unmitigated critical vulnerabilities visible to higher levels of management to ensure the problems are solved. <br> The most effective vulnerability scanning tools compare the results of the current scan with previous scans to determine how the vulnerabilities in the environment have changed over time. Security personnel use these features to conduct vulnerability trending from month to month. <br> As vulnerabilities related to unpatched systems are discovered by scanning tools, security personnel should determine and document the amount of time that elapses between the public release of a patch for the system and the occurrence of the vulnerability scan. If this time window exceeds the entity's benchmarks for deployment of the given patch's criticality level, security personnel should note the delay and determine if a deviation was formally documented for the system and its patch. If not, the security team should work with management to improve the patching process. <br> Additionally, some automated patching tools may not detect or install certain patches due to error by the vendor or administrator. Because of this, all patch checks should reconcile system patches with a list of patches each vendor has announced on its website. |

--- Page 225 ---

| RELEVANT | - Exploitation of known system vulnerabilities |
| :-- | :-- |
| THREATS AND | - Undetected system vulnerabilities |
| VULNERABILITIES | - Unpatched applications |


| T7.7.1 | CONTROL OF <br> TECHNICAL <br> VULNERABILITIES | PRIORITY | P1 |
| :-- | :-- | :-- | :-- |
| T7.7.1 | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |  |
| CONTROL | The entity shall obtain and act upon information about technical <br> vulnerabilities of information systems being used |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify vulnerabilities in new systems and applications and define a <br> remediation plan before placing them in a production environment <br> 2) Test, review, check, and verify the presence of vulnerabilities <br> in production systems throughout the development life-cycle, <br> preferably by the use of automated testing tools <br> 3) Perform a Cost-Benefit-Analysis (CBA) for vulnerabilities to <br> determine the proper remediation plan, where appropriate |  |  |

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

As a prerequisite, a current and complete inventory of assets is needed (including software vendor, version numbers, current state of deployment, and the person(s) within the entity responsible for the software).

The following guidance should be followed to establish an effective management process for technical vulnerabilities:
A. The entity should define and establish the roles and responsibilities associated with technical vulnerability management, including vulnerability monitoring, vulnerability risk assessment (see M2.2), patching, asset tracking, and any coordination responsibilities required
B. The entity should identify information resources that will be used to identify relevant technical vulnerabilities and to maintain awareness about them should be identified for software and other technology (based on the asset inventory list); these information resources should be updated based on changes in the inventory, or when other new or useful resources are found
C. The entity should define a timeline to react to notifications of potentially relevant technical vulnerabilities
D. The entity should identify the risks associated to potential technical vulnerability and the actions to be taken; such action could involve patching of vulnerable systems and/or applying other controls
E. Depending on how urgently a technical vulnerability needs to be addressed, the action taken should be carried out according to the controls related to change management or by following information security incident response procedures
F. If a patch is available, the risks associated with installing the patch should be assessed (the risks posed by the vulnerability should be compared with the risk of installing the patch)

--- Page 226 ---

G. patches should be tested and evaluated before they are installed to ensure they are effective and do not result in side effects that cannot be tolerated; if no patch is available, other controls should be considered, such as
1- turning off services or capabilities related to the vulnerability
2- adapting or adding access controls, e.g. firewalls, at network borders
3- increased monitoring to detect or prevent actual attacks
4- raising awareness of the vulnerability
H. an audit log should be kept for all procedures undertaken
I. the technical vulnerability management process should be regularly monitored and evaluated in order to ensure its effectiveness and efficiency
J. systems at high risk should be addressed first

| T7.8 | SUPPLY CHAIN MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To protect against supply chain threats and secure the supply of information <br> systems |
| PERFORMANCE <br> INDICATOR | Percentage of information systems received within the acceptable time <br> frame and validated as genuine <br> Number of vendors/third parties compliant with the policy for acquisition <br> of products and services |
| AUTOMATION <br> GUIDANCE | An automated support system should be used to support tracking <br> of products and services received and verification of compliance to <br> entity policies |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable supply chain strategy <br> Use of counterfeit or copied software |

--- Page 227 ---

| T7.8.1 | SUPPLY CHAIN <br> PROTECTION <br> STRATEGY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall develop a comprehensive information security strategy against supply chain threats to the information assets. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define a policy to regulate the acquisition of products and services. Such a policy shall include not to disclose to the supplier any unnecessary details about the entity's configurations and architectures <br> 2) Check for every product/service delivered its compliance to security requirements defined by the policy <br> 3) Define in the contract with the supplier that compliance with the entity security policy is required <br> 4) Incentivize transparency into the security practices of the supplier <br> 5) Include the possibility to audit the supplier's security practices <br> 6) Ensure all sector and national level requirements for supply chain security are met |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The use of acquisition and procurement processes by entities early in the system development life cycle provides an important vehicle to protect the supply chain. Entities use available all-source intelligence analysis to inform the tailoring of acquisition strategies, tools, and methods. There are a number of different tools and techniques available (e.g., obscuring the end use of an information system or system component, using blind or filtered buys). Entities also consider creating incentives for suppliers who: <br> A. Implement required security controls <br> B. Promote transparency into their organizational processes and security practices <br> C. Provide additional vetting of the processes and security practices of subordinate suppliers, critical information system components, and services <br> D. Restrict purchases from specific suppliers or countries <br> E. Provide contract language regarding the prohibition of tainted or counterfeit components |  |  |  |  |
| In addition, entities consider minimizing the time between purchase decisions and required delivery to limit opportunities for adversaries to corrupt information system components or products. Finally, entities can use trusted/controlled distribution, delivery, and warehousing options to reduce supply chain risk (e.g., requiring tamper-evident packaging of information system components during shipping and warehousing). |  |  |  |  |

--- Page 228 ---

| T7.8.2 | SUPPLIER REVIEWS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall conduct a supplier review prior to entering into a contractual agreement to acquire the information system, system component, or information system service. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define an evaluation process for suppliers of information systems, system components and services <br> 2) Periodically review supplier evaluations <br> 3) Ensure the supplier review process includes checks with appropriate sector and national level requirements |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Supplier reviews include, for example: <br> A. Analysis of supplier processes used to design, develop, test, implement, verify, deliver, and support information systems, system components, and information system services <br> B. Assessment of supplier training and experience in developing systems, components, or services with the required security capability |  |  |  |  |
| These reviews provide entities with increased levels of visibility into supplier activities during the system development life cycle to promote more effective supply chain risk management. Supplier reviews can also help to determine whether primary suppliers have security controls in place and a practice for vetting subordinate suppliers, for example, second- and third-tier suppliers, and any subcontractors. |  |  |  |  |


| T7.8.3 | LIMITATION OF <br> HARM | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall limit harm from potential adversaries targeting the organizational supply chain. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Limit information shared with suppliers <br> 2) Employ a diverse set of suppliers for any critical information system product and service area |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Supply chain risk is part of the advanced persistent threat. Security controls to reduce the probability of adversaries successfully identifying and targeting the supply chain include, for example: <br> A. Avoiding the purchase of custom configurations to reduce the risk of acquiring information systems, components, or products that have been corrupted via supply chain actions targeted at specific entities <br> B. Employing a diverse set of suppliers to limit the potential harm from any given supplier in the supply chain <br> C. Using procurement carve outs |  |  |  |  |

--- Page 229 ---

| T7.8.4 | SUPPLY CHAIN <br> OPERATIONS <br> SECURITY | PRIORITY |  |
| :-- | :-- | :-- | :-- | :-- |
| CONTROL | The entity shall employ security controls to protect supply chain operations. |  |  |
|  | The entity shall: |  |  |
| SUB-CONTROL | 1) Evaluate risks to its own information systems/services operations <br> considering also threats/vulnerabilities relate to suppliers <br> 2) Work with suppliers to align controls and have them reported in the <br> service contract <br> 3) Define how controls implemented by suppliers will be monitored by <br> the entity |  |  |

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Supply chain information includes, for example: user identities; uses for information systems, information system components, and information system services; supplier identities; supplier processes; security requirements; design specifications; testing and evaluation results; and system/component configurations. This control enhancement expands the scope of operations security (OPSEC) to include suppliers and potential suppliers. OPSEC is a process of identifying critical information and subsequently analyzing friendly actions attendant to operations and other activities to:
A. Identify those actions that can be observed by potential adversaries
B. Determine indicators that adversaries might obtain that could be interpreted or pieced together to derive critical information in sufficient time to cause harm to entities
C. Implement controls or countermeasures to eliminate or reduce to an acceptable level, exploitable vulnerabilities
D. Consider how aggregated information may compromise the confidentiality of users or uses of the supply chain

OPSEC may require entities to withhold critical mission/business information from suppliers and may include the use of intermediaries to hide the end use, or users, of information systems, system components, or information system services.

--- Page 230 ---

| T7.8.5 | RELIABLE DELIVERY | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall ensure a reliable delivery of information systems or system components. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Ensure information systems and components received are genuine <br> 2) Verify software delivered has not being altered |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| For some information system components, especially hardware, there are technical means to help determine if the components are genuine or have been altered. Security controls used to validate the authenticity of information systems and information system components include, for example, optical/nanotechnology tagging and side-channel analysis, hashes comparison mechanisms also can be used to verify if vender or third party software has been altered or not. For hardware, detailed bill of material information can highlight the elements with embedded logic complete with component and production location. |  |  |  |  |


| T7.8.6 | PROCESSES <br> TO ADDRESS WEAKNESSES OR DEFICIENCIES | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall establish a process to address weaknesses or deficiencies in supply chain elements. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Map supply chain elements and identify any interdependency <br> 2) Identify and address any weaknesses or deficiencies during independent or organizational assessments of the mapped supply chain elements <br> 3) Establish a formal review/audit process <br> 4) Conduct regular assessments and audits of supply chain elements |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Evidence generated during independent or organizational assessments of supply chain elements (e.g., penetration testing, audits, verification/validation activities) is documented and used in followon processes implemented by entities to respond to the risks related to the identified weaknesses and deficiencies. Supply chain elements include, for example, supplier development processes and supplier distribution systems. |  |  |  |  |

--- Page 231 ---

| T7.8.7 | SUPPLY OF CRITICAL <br> INFORMATION <br> SYSTEM <br> COMPONENTS | PRIORITY |  |
| :-- | :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall ensure an adequate supply of critical information system and <br> systems components. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Define contingency plan for any supply of critical information <br> system component <br> 2) Stockpiling of critical spare components <br> 3) Use multiple suppliers for critical components |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Adversaries can attempt to impede organizational operations by disrupting the supply of critical <br> information system components or corrupting supplier operations. Controls to ensure adequate <br> supplies of critical information system components include, for example: <br> A. The use of multiple suppliers throughout the supply chain for the identified critical components <br> B. Stockpiling of spare components to ensure operation during mission-critical times |  |  |  |

# T8 INFORMATION SECURITY INCIDENT MANAGEMENT 

| T8 | INFORMATION SECURITY INCIDENT MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure that information security incidents are communicated in a <br> manner allowing timely corrective actions to be taken. |
| PERFORMANCE <br> INDICATOR | Percentage of security incidents reported within the required timeframe <br> and classified according to incident classification policy |


| T8.1 | INFORMATION SECURITY INCIDENT MANAGEMENT POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain an information security incident management policy covering the <br> information security incident procedures covering the detection, reporting <br> and treatment of incidents |
| PERFORMANCE <br> INDICATOR | Extent of information security incident management policy deployment <br> and adoption across the entity |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable or outdated information security incident <br> management policy <br> - Unawareness of information security incident management policy |

--- Page 232 ---

| T8.1.1 | INFORMATION SECURITY INCIDENT MANAGEMENT POLICY | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall establish a policy to manage and guide the response to information security incidents. |  |  |
| SUB-CONTROL | The incident management policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline roles and responsibilities <br> 4) Provide the framework for managing incidents <br> 5) Address sector and national level requirements for handling and reporting incidents <br> 6) Be documented and communicated to all users <br> 7) Be read and acknowledged formally by all users <br> 8) Be maintained, reviewed, exercised and updated at planned intervals or if significant changes occur |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard (also refer to National Cyber Response Framework). |  |  |  |
| The information security incident management policy facilitates the implementation of the associated controls to ensure appropriate reaction to any actual or suspected security incidents relating to information assets. The policy can, for example, contain in addition to the required sub-controls: <br> A. Incident classification <br> B. Procedure for reporting information security events or weaknesses <br> C. Procedure for incident handling |  |  |  |
| The information systems acquisition, development and maintenance policy can be included as part of the general information security policy, in a single policy document, or can be represented by multiple policies reflecting the complex nature of certain entities. |  |  |  |

--- Page 233 ---

| T8.2 | MANAGEMENT OF INFORMATION SECURITY INCIDENTS AND IMPROVEMENTS |
| :--: | :--: |
| OBJECTIVE | To ensure a consistent and effective approach to the management of information security incidents, including communication on security events and weaknesses. |
| PERFORMANCE INDICATOR | Percentage of security incidents that met reporting thresholds, were reported within specified timeframes, and were classified according to the incident classification policy. |
| AUTOMATION GUIDANCE | Incident management and tracking solutions should be considered. They can be very helpful to support teamwork, in particular in large entities. They are also useful for trend analysis and to support management with analysis of threats and of incident impact. |
| RELEVANT THREATS AND VULNERABILITIES | - Lack of incident response training <br> - Inappropriate incident response testing procedures |


| T8.2.1 | INCIDENT <br> RESPONSE PLAN | PRIORITY <br> APPLICABILITY | B2 <br> BASED ON RISK <br> ASSESSMENT |
| :--: | :--: | :--: | :--: |
| CONTROL | The entity shall develop a plan to guide incident response activities. |  |  |
| SUB-CONTROL | The entity shall develop an incident response plan encompassing the following: <br> 1) Processes and procedures for handling incidents before, during, and after an incident occurs to be documented, tested and maintained <br> 2) Communication plan to include internal and external parties <br> 3) Senior management approval of all plans and procedures <br> 4) Required resources and capabilities to be defined <br> 5) Establishment of a Computer Security Incident Response Team (see T8.2.2) |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard (also refer to National Cyber Response Framework). <br> The entity should consider the following: <br> A. Develop an incident response plan that: <br> 1- Provides the entity with a roadmap for implementing its incident response capability <br> 2- Describes the structure and organization of the incident response capability <br> 3- Provides a high-level approach for how the incident response capability fits into the overall entity <br> 4- Meets the unique requirements of the entity, which relate to mission, size, structure, and functions <br> 5- Defines reportable incidents <br> 6- Provides metrics for measuring the incident response capability within the entity <br> 7- Defines the resources and management support needed to effectively maintain and mature an incident response capability <br> 8- Is reviewed and approved by defined personnel or roles |  |  |  |

--- Page 234 ---

B. Make the incident response plan available to defined incident response personnel (identified by name and/or by role- and organizational elements;
C. Review and test the incident response plan in defined frequency;
D. Update the incident response plan to address system/organizational changes or problems encountered during plan implementation, execution, or testing;
E. Communicate incident response plan changes to defined incident response personnel (identified by name and/or by role) and organizational elements; and
F. Protect the incident response plan from unauthorized disclosure and modification.

It is important that entities develop and implement a coordinated approach to incident response. Organizational missions, business functions, strategies, goals, and objectives for incident response help to determine the structure of incident response capabilities. As part of a comprehensive incident response capability, entities consider the coordination and sharing of information with external entities, including, for example, external service providers and entities involved in the supply chain for organizational information systems.

| T8.2.2 | COMPUTER SECURITY INCIDENT RESPONSE TEAM | PRIORITY | P2 |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall establish a Computer Security Incident Response Team (CSIRT) in charge of the incident management and response plan. |  |  |
| SUB-CONTROL | The entity shall establish a CSIRT as follows: <br> 1) Identify stakeholders and participants <br> 2) Secure funding for CSIRT operations <br> 3) Decide on the range and level of services the CSIRT will offer <br> 4) Determine the CSIRT reporting structure, authority, and organizational model <br> 5) Identify required resources such as staff, equipment, and infrastructure <br> 6) Define interactions and interfaces <br> 7) Define roles, responsibilities, and the corresponding authority <br> 8) Document the workflow <br> 9) Develop policies and corresponding procedures <br> 10) Announce the CSIRT when it becomes operational to create the appropriate level of awareness |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard (also refer to National Cyber Response Framework). |  |  |  |
| Entities should identify members in the entity to form the proper CSIRT. The establishment of the team should take place before developing the Incident Response plan. One of the CSIRT's responsibilities is to create the IR Plan. |  |  |  |
| Here are some of the CSIRT members: <br> - Team leader who is usually a senior manager whose responsibility is to take charge of incidents and direct actions to other team members <br> - Boundary protection experts. Normally individuals that are expert in firewalls, routers and IDSs that sits at the edge of the network. |  |  |  |

--- Page 235 ---

- Network administrators
- Physical security members
- Human resources might be involved if the attach was originated by an employee
- Communication might be involved to become the public face for incidents that became public.

Here are some of the primary responsibilities of the CSIRT:

- Develop incident policy, plan, and procedures
- Response to incidents and minimizing the impact
- Investigate incidents and determine the cause
- prevent future incident by recommending security controls
- Handle incident reporting and communication to all stakeholder involved internally and externally
- Protect collected evidence

| T8.2.3 | INCIDENT <br> CLASSIFICATION | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall assess and classify information security incidents. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish an incident classification scheme in line with the incident response policy taking into account NESA's issuances with regard to incident management <br> 2) Assess and identify the incidents that should be reported at the sector and national level |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Classification and prioritization of incidents can help to identify the impact and extent of an incident. A point of contact should assess the information security events using the agreed information security event and incident classification scale and decide whether the events should be classified as information security incidents. <br> In case where the entity has CSIRT, the assessment and decision can be forwarded to the CSIRT for confirmation or reassessment. Results of the assessment and decision should be recorded in detail for the purpose of future reference and verification. <br> An attack is classified as an incident if the attack is directed against information assets, has a realistic chance of success and threatens the confidentiality, integrity and availability of information resources and assets. <br> An indication of an incident can be one or more of the following: <br> - If dormant or inactive accounts started accessing system resources, querying servers, or engaged in other activities <br> - If modification of logs occurs and the systems administrator cannot determine explicitly the authorized individual who modified them <br> - Presence of hacking tools <br> - Notifications by partner or peer <br> - Notification by the attacker |  |  |  |  |

--- Page 236 ---

| T8.2.4 | INCIDENT <br> RESPONSE <br> TRAINING | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall provide incident response training to information system users. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish a training program for the cyber security incident response team (CSIRT), in line with the Awareness and Training Policy (refer to M3.1.1) <br> 2) Ensure that the program covers all incident response procedures as well as their users |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| In designing the incident response training, entities should customize the content and level of details based on the targeted audience to allow attendees to focus on the information that is relevant to them. <br> As such, end users may only need to identify an incident or suspicious activities and call the right contact, system administrators may require technical training on how to handle/remediate incidents, and incident responders may receive more specific training on forensics, reporting, system recovery, and restoration. |  |  |  |  |


| T8.2.5 | INCIDENT <br> RESPONSE TESTING | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall test its incident response capability. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop testing procedures and cases to validate effectiveness and usefulness of its incident response capability <br> 2) Establish expected test results <br> 3) Conduct incident response capability testing and compare outcome to the expected results to identify gaps and weaknesses for remediation |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The entity should develop testing procedures to determine the overall effectiveness of its incident response capabilities and to identify potential weaknesses or deficiencies. Incident response testing must simulate pre-defined breach scenarios across the incident response lifecycle from including detection, reporting, and recovery to normal operations. Incident response testing includes, for example, the use of checklists, tabletop (discussion-based) exercises, and functional (performance of duties in a simulated environment) exercises. Entities should participate in sector, national, and international exercises to further test incident response capabilities. |  |  |  |  |

--- Page 237 ---

| T8.2.6 | INCIDENT <br> RESPONSE <br> ASSISTANCE | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall provide an incident response support resource to offer advice and assistance in case of an incident. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Develop testing procedures and cases to validate effectiveness and usefulness of its incident response capability <br> 2) Establish expected test results <br> 3) Conduct incident response capability testing and compare outcome to the expected results to identify gaps and weaknesses for remediation |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| The entity should provide an incident response support resources as part of its incident response capability to provide advice and assistance to users of the information system during steady state operation and incidents for the detection, handling and reporting of security incidents. <br> The entity should provide an incident response support resources in different forms to reach the widest audience, such as: <br> - Informative website <br> - Online knowledge base <br> - Call center, etc. <br> Moreover, the entity should coordinate with external providers (for example, national CERT) through its incident response capability for help in the detection and handling of incidents within the entity. |  |  |  |  |


| T8.2.7 | INFORMATION SECURITY INCIDENT DOCUMENTATION | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall document all information security incidents. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the relevant data to be collected before, during and after an information security incident takes place <br> 2) Collect and document relevant data related to all security incidents <br> 3) Protect the information security incident documentation |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Documenting information security incidents includes, for example, maintaining records about each incident, the status of the incident, and other pertinent information necessary for forensics, evaluating incident details, trends, and handling. Incident information can be obtained from a variety of sources including, for example, incident reports, incident response teams, audit monitoring, network monitoring, physical access monitoring, and user/administrator reports |  |  |  |  |

--- Page 238 ---

| T8.2.8 | LEARNING FROM <br> INFORMATION <br> SECURITY <br> INCIDENTS | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall institutionalize the learning from information security incidents. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish detailed incident records including all related activities and outcomes where applicable <br> 2) Develop lessons learned and where applicable identify additional controls to avoid similar incidents in the future |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| There should be mechanisms in place to enable the types, volumes, costs, and impacts of information security incidents to be quantified and monitored. The information gained from the evaluation of information security incidents should be used to identify recurring or high impact incidents and inform risk assessment and risk treatment activities. <br> Investigations based on information distributed by an information sharing community should be performed, to reduce the risks of similar incidents and develop a better understanding of the risks facing the community and any related significant information infrastructures. Such investigations could be performed by the community members involved, or by a supporting entity, if one exists. <br> Following reported incidents, post incident reviews should be performed by members of the information sharing community to trigger updates to security incident response plans, related procedures and the business risk profile, and implementation of additional controls even if the member was not affected by the incident in question. Each member should ensure that reported incident responses are assessed, and any lessons or possible improvements to the member's own processes are identified and acted upon to continuously improve its own response processes. |  |  |  |

![img-13.jpeg](img-13.jpeg)

--- Page 239 ---

| T8.2.9 | COLLECTION OF <br> EVIDENCE | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall identify, collect, and preserve the information, which can serve as evidence. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify the requirements of the applicable jurisdictions <br> 2) Establish procedures for collecting evidence taking into account : <br> - Chain of custody <br> - Safety of evidence <br> - Safety of the personnel <br> - Roles and responsibilities of personnel involved <br> - Competency of the personnel <br> - Documentation <br> - Briefing <br> - Other identified requirements |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Internal procedures should be developed and followed when dealing with evidence for the purposes of disciplinary and legal action. |  |  |  |  |
| Identification is the process involving the search for, recognition and documentation of potential evidence. Collection is the process of gathering the physical items that can contain potential evidence. Acquisition is the process of creating a copy of data within a defined set. Preservation is the process to maintain and safeguard the integrity and original condition of the potential evidence. |  |  |  |  |
| In general, the procedures for evidence should provide processes of identification, collection, acquisition and preservation in accordance with different types of media, devices and status of devices, e.g., powered on or off. The procedures should take account of: <br> A Chain of custody <br> B Safety of evidence <br> C Safety of the personnel <br> D Roles and responsibilities of personnel involved <br> E Competency of the personnel <br> F Documentation <br> G Briefing |  |  |  |  |
| Where available, certification or other relevant means of qualification of personnel and tools should be sought, so as to strengthen the value of the preserved evidence. |  |  |  |  |
| Forensic evidence may transcend organizational or jurisdictional boundaries. In such cases, it should be ensured that the entity is entitled to collect the required information as forensic evidence. The requirements of different jurisdictions should also be considered to maximize chances of admission across the relevant jurisdictions. |  |  |  |  |

--- Page 240 ---

| T8.3 | INFORMATION SECURITY EVENTS AND WEAKNESSES REPORTING |
| :--: | :--: |
| OBJECTIVE | To ensure information security events and weaknesses associated with information systems are communicated in a manner allowing timely corrective action to be taken |
| PERFORMANCE INDICATOR | Percentage of information security incidents reported within the required time frame per applicable incident category as defined in the information security incident management policy |
| AUTOMATION GUIDANCE | For an automated identification of weaknesses, a large number of vulnerability scanning tools are available. Some enterprises have also found commercial services using remotely managed scanning appliances to be effective. To help standardize the definitions of discovered vulnerabilities in multiple departments of an entity or even across entities, it is preferable to use vulnerability scanning tools that measure security flaws and map them to vulnerabilities and issues categorized using one or more of the following industry-recognized vulnerability, configuration, and platform classification schemes and languages: CVE, CCE, OVAL, CPE, CVSS, and/or XCCDF. |
|  | Advanced vulnerability scanning tools can be configured with user credentials to log in to scanned systems and perform more comprehensive scans than can be achieved without login credentials. The frequency of scanning activities, however, should increase as the diversity of an entity's systems increases to account for the varying patch cycles of each vendor. |
|  | Also, event log collectors and incident management systems should be considered. These technologies provide log collection, normalization, correlation and analysis: they can be very helpful both to detect incidents in their early stages and to investigate incidents. |
| RELEVANT THREATS AND VULNERABILITIES | - Leakage of reported weaknesses <br> - Unsuitable reporting procedures |

--- Page 241 ---

| T8.3.1 | SITUATIONAL <br> AWARENESS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall develop a situational awareness culture by participating in the information sharing community and obtaining cyber security information from various sources. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify priority information and share it internally to build the entity context <br> 2) For the sector context, identify and share priority information that is relevant to entities in the same sector to build the sector context <br> 3) For the national context, identify and share priority information that is relevant across all sectors to build the national context |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Critical entities shall also take into account any other NESA relevant issuances, guidance, and activities in this regard (also refer to National Cyber Response Framework, and National Cyber Information Sharing Policy). |  |  |  |  |
| Priority information is information that may enable other community members to avoid or minimize similar undesirable events. It is important that such information is shared urgently, even if it is not fully analyzed or confirmed. The legal department, security vendors, third-party cyber threat intelligence providers, as well as the regulator should discuss what information can be shared and with whom. |  |  |  |  |


| T8.3.2 | REPORTING <br> INFORMATION <br> SECURITY EVENTS | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall report information security events through appropriate management channels. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify a designated event point of contact (e.g. CSIRT) <br> 2) Establish an information security events reporting procedure <br> 3) Establish an event communication and reporting approach to the appropriate stakeholder (including appropriate authority) <br> 4) Ensure the reporting approach accounts for all sector and national level management channels |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| All employees and external party users should be made aware of their responsibility to report any information security events as quickly as possible. They should also be aware of the procedure for reporting information security events and the point of contact (POC) where the events should be reported to. |  |  |  |  |

--- Page 242 ---

Situations to be considered for information security event reporting include:
A. Ineffective security control
B. Breach of information integrity, confidentiality or availability expectations
C. Human errors
D. Non-compliances with policies or guidelines
E. Breaches of physical security arrangements
F. Uncontrolled system changes
G. Malfunctions of software or hardware
H. Access violations

| T8.3.3 | REPORTING SECURITY WEAKNESSES | PRIORITY |  | P4 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall report observed or suspected information security weaknesses in systems or services. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish and make available a procedure for employees and external third party users to report information security weaknesses as soon as identified <br> 2) Establish a CSIRT as a point of contact for any information security related issue <br> 3) Ensure that no user is trying to exploit the weakness |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| A security weakness (or vulnerability) is a flow which allows an attacker to reduce a system's information assurance. |  |  |  |  |
| All employees, contractors and external party users should report these matters to the point of contact as quickly as possible in order to prevent information security incidents. The reporting mechanism should be as easy, accessible and available as possible. They should be informed that they should not, in any circumstances, attempt to prove a suspected weakness. Testing weaknesses might be interpreted as a potential misuse of the system and could also cause damage to the information system or service and result in legal liability for the individual performing the testing. |  |  |  |  |

--- Page 243 ---

# T9 INFORMATION SYSTEMS CONTINUITY MANAGEMENT 

| T9 | INFORMATION SYSTEMS CONTINUITY MANAGEMENT |
| :-- | :-- |
| OBJECTIVE | To ensure business continuity and protection of critical information |
| PERFORMANCE <br> INDICATOR | Percentage of information assets with measured availability above the <br> minimum acceptable thresholds |


| T9.1 | INFORMATION SYSTEMS CONTINUITY MANAGEMENT POLICY |
| :-- | :-- |
| OBJECTIVE | To maintain an information continuity management policy covering the <br> continuity and redundancy of information based on their level of criticality |
| PERFORMANCE <br> INDICATOR | Percentage of organizational units with an established information <br> continuity plan in accordance with the information continuity <br> management policy |
| AUTOMATION <br> GUIDANCE | Not applicable |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unsuitable information systems continuity management policy <br> - Unawareness of information systems continuity management policy <br> among IT staff |


| T9.1.1 | INFORMATION SYSTEMS CONTINUITY PLANNING POLICY | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |
| CONTROL | The entity shall establish an information systems continuity planning policy. |  |  |
| SUB-CONTROL | The information systems continuity planning policy shall: <br> 1) Be appropriate to the purpose of the entity <br> 2) Include statement of the management commitment, purpose, objective and scope of the policy <br> 3) Outline roles and responsibilities <br> 4) Provide the framework for continuity of information in adverse situations in accordance with the entity overall business continuity and / or disaster recovery planning <br> 5) Be documented and communicated to all users <br> 6) Be read and acknowledged formally by all users <br> 7) Be maintained, reviewed, tested and updated at planned intervals or if significant changes occur |  |  |

--- Page 244 ---

# IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) 

Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard.

An entity should determine whether the continuity of information security is captured within the BCM process or within the (IT) disaster recovery management (DRM- process. Information security requirements should be determined when planning for business continuity and disaster recovery.

In the absence of formal business continuity and disaster recovery planning, information security management should assume that information security requirements remain the same in adverse situations, compared to normal operational conditions. Alternatively, an organization could perform a business impact analysis (BIA- for information security aspects to determine the information security requirements applicable to adverse situations.

The process of including information security in the business continuity management should bring together the following key elements of business continuity management:
A. Understanding the risks the entity is facing in terms of likelihood and impact in time, including an identification and prioritization of critical business processes
B. Identifying all the assets involved in critical business processes
C. Understanding the impact which interruptions caused by information security incidents are likely to have on the business (it is important that solutions are found that will handle incidents causing smaller impact, as well as serious incidents that could threaten the viability of the entity), and establishing the business objectives of information systems
D. Considering the purchase of suitable insurance which may form part of the overall business continuity process, as well as being part of operational risk management
E. Identifying and considering the implementation of additional preventive and mitigating controls
F. Identifying sufficient financial, organizational, technical, and environmental resources to address the identified information security requirements
G. Ensuring the safety of personnel and the protection of information systems and organizational property

The process should bring together the following key elements of business continuity management:
A. Formulating and documenting business continuity plans addressing information security requirements in line with the agreed business continuity strategy;
B. Regular testing and updating of the plans and processes put in place;
C. Ensuring that the management of business continuity is incorporated in the entity's processes and structure; responsibility for the business continuity management process should be assigned at an appropriate level within the entity.

--- Page 245 ---

| T9.2 | INFORMATION SECURITY ASPECTS OF INFORMATION CONTINUITY MANAGEMENT |
| :--: | :--: |
| OBJECTIVE | To counteract interruptions to business activities and to protect critical business processes from the effects of major failures of information systems or disasters and to ensure their timely resumption |
| PERFORMANCE INDICATOR | Percentage of organizational units with information continuity plans that have been adequately documented and proven by suitable testing |
| AUTOMATION GUIDANCE | Not applicable |
| RELEVANT THREATS AND VULNERABILITIES | - Destruction of equipment or media <br> - Corruption of data |


| T9.2.1 | DEVELOPING <br> INFORMATION <br> SYSTEMS <br> CONTINUITY PLANS | PRIORITY |  |
| :-- | :-- | :-- | :-- |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall develop its information systems continuity plans. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Identify information continuity requirements in line with the entity's <br> overall business continuity planning and / or disaster recovery <br> 2) Specify the escalations criteria and the conditions for its activation <br> 3) Outline information continuity roles and responsibilities, and assign <br> individuals with contact information <br> 4) Define a safe mode when incidents are detected that restrict the <br> entity's operation in accordance with the information systems <br> continuity policy |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| Critical entities shall also take into account any other NESA's relevant issuances, guidance, and activities in this regard. |  |  |  |
| The continuity planning process should consider the following: <br> A. Identification and agreement of all responsibilities and continuity procedures <br> B. Identification of the acceptable loss of information and services <br> C. Implementation of the procedures to allow recovery and restoration of business operations <br> and availability of information in required time-scales; particular attention needs to be <br> given to the assessment of internal and external business dependencies and the contracts <br> in place <br> D. Operational procedures to follow pending completion of recovery and restoration <br> E. Documentation of agreed procedures and processes <br> F. Appropriate education of staff in the agreed procedures and processes, including <br> crisis management <br> G. Testing and updating of the plans |  |  |  |

--- Page 246 ---

The planning process should focus on the required business objectives, e.g. restoring of specific communication services to customers in an acceptable amount of time. The services and resources facilitating this should be identified, including staffing, non-information processing resources, as well as fallback arrangements for information systems. Such fallback arrangements may include arrangements with third parties in the form of reciprocal agreements, or commercial subscription services.

If alternative temporary locations are used, the level of implemented security controls at these locations should be equivalent to the main site.

| T9.2.2 | IMPLEMENTING <br> INFORMATION <br> SYSTEMS <br> CONTINUITY PLANS | PRIORITY |  |
| :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK <br> ASSESSMENT |
| CONTROL | The entity shall implement for the established information security plans. |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Establish information systems continuity capabilities based on the established plans |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |
| An entity should ensure that: <br> A. An adequate management structure is in place to prepare for, mitigate and respond to a disruptive event using personnel with the necessary authority, experience and competence <br> B. Incident response personnel with the necessary responsibility, authority and competence to manage an incident and maintain information security is nominated <br> C. Documented plans, response and recovery procedures are developed and approved, detailing how the entity will manage a disruptive event and will maintain its information security to a predetermined level, based on management-approved information security (continuity) objectives |  |  |  |
| According to the information security continuity requirements, the entity should establish, document, implement and maintain: <br> A. information security controls within business continuity and/or disaster recovery processes, procedures and supporting (information- systems and tools <br> B. processes, procedures and implementation changes to maintain existing information security controls during an adverse situation <br> C. compensating controls for information security controls that cannot be maintained during an adverse situation |  |  |  |

--- Page 247 ---

| T9.3 | TESTING, MAINTAINING AND REASSESSING PLANS |
| :-- | :-- |
| OBJECTIVE | To ensure the effectiveness of the information systems continuity <br> management plans and they are always up-to-date |
| PERFORMANCE <br> INDICATOR | Percentage of information systems that went through an annual testing |
| AUTOMATION <br> GUIDANCE | An automated solution to plan tests and to keep track of the results and the <br> improvement areas should be considered. |
| RELEVANT <br> THREATS AND <br> VULNERABILITIES | - Unperformed information systems continuity management testing <br> - Outdated information systems continuity management plan |


| T9.3.1 | TESTING, MAINTAINING AND RE-ASSESSING INFORMATION SYSTEMS CONTINUITY PLANS SYSTEMS CONTINUITY PLANS | PRIORITY |  | P3 |
| :--: | :--: | :--: | :--: | :--: |
|  |  | APPLICABILITY | BASED ON RISK ASSESSMENT |  |
| CONTROL | The entity shall test, maintain and re-assess its information systems continuity plans. |  |  |  |
| SUB-CONTROL | The entity shall: <br> 1) Periodically test the continuity plan for the information systems following the established procedures to determine the effectiveness of the plan and the organizational readiness to execute the plan <br> 2) Establish lessons learned and update the information systems continuity plans to ensure they are always up-to-date |  |  |  |
| IMPLEMENTATION GUIDANCE (FOR INFORMATION PURPOSE ONLY) |  |  |  |  |
| Business continuity plan tests should ensure that all members of the recovery team and other relevant staff are aware of the plans and their responsibility for business continuity and information security and know their role when a plan is invoked. <br> The test schedule for business continuity plan(s) should indicate how and when each element of the plan should be tested. Each element of the plan(s) should be tested frequently. <br> A variety of techniques should be used in order to provide assurance that the plan(s) will operate in real life. These should include: <br> A. Table-top testing of various scenarios (discussing the business recovery arrangements using example interruptions) <br> B. Simulations (particularly for training people in their post-incident/crisis management roles) <br> C. Technical recovery testing (ensuring information systems can be restored effectively) <br> D. Testing recovery at an alternate site (running business processes in parallel with recovery operations away from the main site) |  |  |  |  |

--- Page 248 ---

E. Tests of supplier facilities and services (ensuring externally provided services and products will meet the contracted commitment)
F. Complete rehearsals (testing that the entity, personnel, equipment, facilities, and processes can cope with interruptions)

These techniques can be used by any entity. They should be applied in a way that is relevant to the specific recovery plan. The results of tests should be recorded and actions taken to improve the plans, where necessary.

Responsibility should be assigned for regular reviews of each business continuity plan. The identification of changes in business arrangements not yet reflected in the business continuity plans should be followed by an appropriate update of the plan. This formal change control process should ensure that the updated plans are distributed and reinforced by regular reviews of the complete plan.

Examples of changes where updating of business continuity plans should be considered are acquisition of new equipment, upgrading of systems and changes in:

- Personnel
- Addresses or telephone numbers
- Business strategy
- Location, facilities, and resources
- Legislation
- Contractors, suppliers, and key customers
- Processes, or new or withdrawn ones
- Risk (operational and financial)

[^0]
[^0]:    Most of this information is derived from a variety of sources, including:

    - ISO/IEC 27001:2005 "Information technology - Security techniques - Information security management systems - Requirements"
    - ISO/IEC 27002:2005 "Information technology - Security techniques - Code of practice for Information security management"
    - ISO/IEC 27005:2005 "Information technology - Security techniques - Information security risk management"
    - ISO/IEC 27010:2012 "Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications"
    - ISO/IEC 27032:2012 "Information technology - Security techniques - Guidelines for cybersecurity"
    - NIST Special Publication 800-53 Revision 4 "Security and Privacy Controls for Federal Information Systems and Organizations"
    - Abu Dhabi Information Security Standards Version 1 and Version 2, developed by Abu Dhabi Systems and Information Centre (ADSIC)
    - SANS 20 Critical Security Controls for Effective Cyber Defense Version 4.1

--- Page 249 ---

# 1.1.2.2.2.2.2.3.2.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.2.3.1.2.3.2.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.3.2.1.2.3.2.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.3.2.2.3.2.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.3.3.1.2.3.3.2.3.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.4.1.2.4.1.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.4.3.1.2.4.3.2.4.3.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.5.1.2.5.2.5.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.5.2.1.2.5.2.5.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.6.1.2.6.1.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.6.2.1.2.6.2.6.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.7.1.2.7.1.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.7.2.1.2.7.2.7.3.4.1.7.1.7.2.7.3.4.1.8. 

## 1.1.2.8.1.2.8.1.3.4.1.7.1.7.2.8.1.8. 

## 1.1.2.8.2.1.2.8.2.8.3.4.1.7.1.7.2.8.1.8. 

## 1.1.2.9.1.2.9.1.3.4.1.7.1.7.2.9.1.8. 

## 1.1.2.9.2.1.2.9.2.1.3.4.1.7.1.7.2.9.1.8. 

## 1.1.2.9.2.2.2.2.2.3.4.1.7.1.7.2.9.1.8. 

## 1.1.2.10.1.2.10.1.3.4.1.7.1.7.2.10.1. 

## 1.1.2.10.2.1.2.1.3.4.1.7.1.7.2.10.1. 

## 1.1.2.11.1.2.11.1.3.4.1.7.1.7.2.11.1. 

## 1.1.2.11.3.1.3.1.3.4.1.7.1.7.2.11.1. 

## 1.1.2.11.4.1.3.4.1.7.1.7.2.11.1. 

## 1.1.2.12.1.2.1.3.4.1.7.1.7.2.12.1. 

## 1.1.2.12.2.1.3.4.1.7.1.7.2.12.1. 

## 1.1.2.13.1.3.1.3.4.1.7.1.7.2.13.1. 

## 1.1.2.13.2.1.3.4.1.7.1.7.2.13.1. 

## 1.1.2.14.1.1.3.4.1.7.1.7.2.14.1. 

## 1.1.2.14.2.1.3.4.1.7.1.7.2.14.1. 

## 1.1.2.15.1.1.3.4.1.7.1.7.2.15.1. 

## 1.1.2.15.2.1.3.4.1.7.1.7.2.15.1. 

## 1.1.2.15.2.1.3.4.1.7.1.7.2.15.1. 

## 1.1.2.16.1.1.3.4.1.7.1.7.2.16.1. 

## 1.1.2.16.2.1.3.4.1.7.1.7.2.16.1. 

## 1.1.2.17.1.1.3.4.1.7.1.7.2.17.1. 

## 1.1.2.17.2.1.3.4.1.7.1.7.2.17.1. 

## 1.1.2.17.3.1.3.4.1.7.1.7.2.17.1. 

## 1.1.2.18.1.1.3.4.1.7.1.7.2.18.1. 

## 1.1.2.18.2.1.3.4.1.7.1.7.2.18.1. 

## 1.1.2.19.1.1.3.4.1.7.1.7.2.19.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 

## 1.1.2.20.1.1.3.4.1.7.1.7.2.1. 



--- Page 250 ---

# 6 

![img-14.jpeg](img-14.jpeg)

--- Page 251 ---

# 0 

![img-15.jpeg](img-15.jpeg)

--- Page 252 ---

# ANNEXA 

## SUMMARY OF ALWAYS APPLICABLE CONTROLS

The following table provides a list of "Always Applicable" security controls. As a recap, "Always Applicable" security controls represent critical requirements for building foundational IA capabilities and must be implemented by each relevant entity regardless of its risk assessment outcomes. Omission of any of these security controls constitutes non-conformity to this Standard.

Overall, a total of 34 management controls constitute the list of "Always Applicable" controls as outlined in Table 5 below.

## TABLE 5: SUMMARY OF ALWAYS APPLICABLE CONTROLS

## CONTROL

NUMBER

## M1

M1.1
M1.1.1
M1.1.2
M1.1.3

## M1.2

M1.2.1
M1.2.2

## M1.4

M1.4.1
M1.4.2
M1.4.3

## M2

M2.1
M2.1.1

## M2.2

M2.2.1
M2.2.2
M2.2.3

## M2.3

M2.3.1
M2.3.2

## CONTROL

NAME

## STRATEGY AND PLANNING

ENTITY CONTEXT AND LEADERSHIP
Understanding the Entity and its Context
Leadership and Management Commitment
Roles and Responsibilities for Information Security

INFORMATION SECURITY POLICY
Information Security Policy
Supporting Policies for Information Security

SUPPORT
Resources
Internal and External Communication
Documentation

INFORMATION SECURITY RISK MANAGEMENT
INFORMATION SECURITY RISK MANAGEMENT POLICY
Information Security Risk Management Policy

INFORMATION SECURITY RISK ASSESSMENT
Information Security Risk Identification
Information Security Risk Analysis
Information Security Risk Evaluation

INFORMATION SECURITY RISK TREATMENT
Information Security Risk Treatment Options
Identification of Controls

--- Page 253 ---

| CONTROL | CONTROL |
| :-- | :-- |
| NUMBER | NAME |
| M2.3.3 | Risk Treatment Plan |
| M2.3.4 | Statement of Applicability |
| M2.3.5 | Information Security Objectives |
| M2.4 | ONGOING INFORMATION SECURITY RISK MANAGEMENT |
| M2.4.1 | Risk Monitoring and Review |
| M2.4.2 | Risk Communication and Consultation |
| M3 | AWARENESS AND TRAINING |
| M3.2 | AWARENESS AND TRAINING PLANNING |
| M3.2.1 | Awareness and Training Program |
| M3.3 | SECURITY TRAINING |
| M3.3.1 | Training Needs |
| M3.3.2 | Implementation Plan |
| M3.3.3 | Training Execution |
| M4 | HUMAN RESOURCES SECURITY |
| M4.1 | HUMAN RESOURCES SECURITY POLICY |
| M4.1.1 | Human Resources Security Policy |
| M4.2 | PRIOR TO EMPLOYMENT |
| M4.2.1 | Screening |
| M4.2.2 | Terms and Conditions of Employment |
| M4.3 | DURING EMPLOYMENT |
| M4.3.1 | Management Responsibilities |
| M4.3.2 | Disciplinary Process |
| M4.4 | TERMINATION OR CHANGE OF EMPLOYMENT |
| M4.4.1 | Termination Responsibilities |
| M4.4.2 | Return of Assets |
| M4.4.3 | Removal of Access Rights |
| M6 | PERFORMANCE EVALUATION AND IMPROVEMENT |
| M6.2 | PERFORMANCE EVALUATION |
| M6.2.1 | Monitoring, Measurement, Analysis and Evaluation |
| M6.2.2 | Internal Audits |
| M6.3 | IMPROVEMENT |
| M6.3.1 | Corrective Action |
| M6.3.2 | Continual Improvement |
|  |  |

--- Page 254 ---

# ANNEX B 

## SUMMARY OF THE PRIORITIZED CONTROLS

The following table provides a list of the prioritized security controls. As a recap, the concept of "Prioritization" relates to grouping the security controls in order of importance for realizing a minimum level of information assurance protection, and for enabling a phased and incremental implementation of this Standard.

Overall, the distribution of security controls across the four priority levels is outlined in Table 6, and the detailed listing is provided in Table 7, below.

TABLE 6: DISTRIBUTION OF SECURITY CONTROLS ACROSS PRIORITY LEVELS

| PRIORITY <br> LEVEL | NUMBER OF CONTROLS |
| :--: | :--: |
| P1 | 39 |
| P2 | 69 |
| P3 | 35 |
| P4 | 45 |

--- Page 255 ---

# TABLE 7: SUMMARY OF PRIORITIZED CONTROLS 

## CONTROL CONTROL NUMBER NAME

## P1 CONTROLS

M1.1.1 UNDERSTANDING THE ENTITY AND ITS CONTEXT
M1.1.2 LEADERSHIP AND MANAGEMENT COMMITMENT
M1.1.3 ROLES AND RESPONSIBILITIES FOR INFORMATION SECURITY
M1.2.1 INFORMATION SECURITY POLICY
M1.3.5 IDENTIFICATION OF RISKS RELATED TO EXTERNAL PARTIES
M1.4.1 RESOURCES
M2.1.1 INFORMATION SECURITY RISK MANAGEMENT POLICY
M2.2.1 INFORMATION SECURITY RISK IDENTIFICATION
M2.2.2 INFORMATION SECURITY RISK ANALYSIS
M2.2.3 INFORMATION SECURITY RISK EVALUATION
M2.3.1 INFORMATION SECURITY RISK TREATMENT OPTIONS
M2.3.2 IDENTIFICATION OF CONTROLS
M2.3.3 RISK TREATMENT PLAN
M2.3.4 STATEMENT OF APPLICABILITY
M2.4.1 RISK MONITORING AND REVIEW
M2.4.2 RISK COMMUNICATION AND CONSULTATION
M3.3.1 TRAINING NEEDS
M4.4.1 TERMINATION RESPONSIBILITIES
M4.4.2 RETURN OF ASSETS
M4.4.3 REMOVAL OF ACCESS RIGHTS

T1.4.1 MANAGEMENT OF REMOVABLE MEDIA
T3.4.1 CONTROLS AGAINST MALWARE
T3.5.1 INFORMATION BACKUP
T3.6.3 MONITORING SYSTEM USE
T4.5.1 NETWORK CONTROLS
T4.5.3 SEGREGATION IN NETWORKS
T5.2.1 USER REGISTRATION
T5.2.2 PRIVILEGE MANAGEMENT
T5.2.3 USER SECURITY CREDENTIALS MANAGEMENT
T5.2.4 REVIEW OF USER ACCESS RIGHTS
T5.3.1 USE OF SECURITY CREDENTIALS
T5.4.2 USER AUTHENTICATION FOR EXTERNAL CONNECTIONS
T5.4.3 EQUIPMENT IDENTIFICATION IN NETWORKS
T5.4.5 NETWORK CONNECTION CONTROL
T5.5.1 SECURE LOG-ON PROCEDURES
T5.5.2 USER IDENTIFICATION AND AUTHENTICATION
T5.5.3 USER CREDENTIALS MANAGEMENT SYSTEM
T5.6.1 INFORMATION ACCESS RESTRICTION
T7.7.1 CONTROL OF TECHNICAL VULNERABILITIES

--- Page 256 ---

# CONTROL CONTROL <br> NUMBER NAME 

## P2 CONTROLS

M1.2.2 SUPPORTING POLICIES FOR INFORMATION SECURITY
M1.3.1 AUTHORIZATION PROCESS FOR INFORMATION SYSTEMS
M1.3.2 CONFIDENTIALITY AGREEMENTS
M1.3.6 ADDRESSING SECURITY WHEN DEALING WITH CUSTOMERS
M1.3.7 ADDRESSING SECURITY IN THIRD PARTY AGREEMENTS
M1.4.2 INTERNAL AND EXTERNAL COMMUNICATION
M1.4.3 DOCUMENTATION
M2.3.5 INFORMATION SECURITY OBJECTIVES
M3.1.1 AWARENESS AND TRAINING POLICY
M3.2.1 AWARENESS AND TRAINING PROGRAM
M3.3.3 TRAINING EXECUTION
M5.2.6 REGULATION OF CRYPTOGRAPHIC CONTROLS
M5.4.1 TECHNICAL COMPLIANCE CHECKING
M6.2.1 MONITORING, MEASUREMENT, ANALYSIS AND EVALUATION
M6.2.2 INTERNAL AUDITS
M6.3.1 CORRECTIVE ACTION
M6.3.2 CONTINUAL IMPROVEMENT
T1.1.1 ASSET MANAGEMENT POLICY
T1.2.1 INVENTORY OF ASSETS
T1.2.2 OWNERSHIP OF ASSETS
T1.2.3 ACCEPTABLE USE OF ASSETS
T1.2.4 ACCEPTABLE BRING YOUR OWN DEVICE (BYOD) ARRANGEMENTS
T1.4.2 DISPOSAL OF MEDIA
T2.2.1 PHYSICAL SECURITY PERIMETER
T2.2.2 PHYSICAL ENTRY CONTROLS
T2.2.3 SECURING OFFICES, ROOMS AND FACILITIES
T2.3.1 EQUIPMENT SITING AND PROTECTION
T2.3.8 UNATTENDED USER EQUIPMENT
T3.2.1 COMMON SYSTEMS CONFIGURATION GUIDELINES
T3.2.4 SEGREGATION OF DUTIES
T3.2.5 SEPARATION OF DEVELOPMENT, TEST AND OPERATIONAL FACILITIES
T3.6.2 AUDIT LOGGING
T3.6.4 PROTECTION OF LOG INFORMATION
T3.6.5 ADMINISTRATOR AND OPERATOR LOGS
T4.2.1 INFORMATION TRANSFER PROCEDURES

--- Page 257 ---

# CONTROL CONTROL <br> NUMBER NAME 

T4.3.1 ELECTRONIC COMMERCE
T4.5.2 SECURITY OF NETWORK SERVICES
T4.5.4 SECURITY OF WIRELESS NETWORKS
T5.1.1 ACCESS CONTROL POLICY
T5.4.1 POLICY ON USE OF NETWORK SERVICES
T5.4.7 WIRELESS ACCESS
T5.6.2 SENSITIVE SYSTEM ISOLATION
T6.2.1 SERVICE DELIVERY
T6.2.2 MONITORING AND REVIEW OF THIRD PARTY SERVICES
T6.2.3 MANAGING CHANGES TO THIRD PARTY SERVICES
T6.3.1 INFORMATION SECURITY REQUIREMENTS FOR CLOUD ENVIRONMENTS
T6.3.2 SERVICE DELIVERY AGREEMENTS WITH CLOUD PROVIDERS
T7.3.1 INPUT DATA VALIDATION
T7.3.2 CONTROL OF INTERNAL PROCESSING
T7.3.3 MESSAGE INTEGRITY
T7.3.4 OUTPUT DATA VALIDATION
T7.4.1 POLICY ON THE USE OF CRYPTOGRAPHIC CONTROLS
T7.4.2 KEY MANAGEMENT
T7.6.3 RESTRICTIONS ON CHANGES TO SOFTWARE PACKAGES
T7.6.4 INFORMATION LEAKAGE
T 8.1.1 INFORMATION SECURITY INCIDENT MANAGEMENT POLICY
T8.2.1 INCIDENT RESPONSE PLAN
T8.2.2 COMPUTER SECURITY INCIDENT RESPONSE TEAM

--- Page 258 ---

# CONTROL CONTROL NUMBER NAME 

## P3 CONTROLS

M3.3.2 IMPLEMENTATION PLAN
M5.2.4 DATA PROTECTION AND PRIVACY OF PERSONAL INFORMATION
M5.2.5 PREVENTION OF MISUSE OF INFORMATION SYSTEMS
M6.1.1 PERFORMANCE EVALUATION POLICY
T1.3.1 CLASSIFICATION OF INFORMATION
T1.3.2 LABELING OF INFORMATION
T1.3.3 HANDLING OF INFORMATION ASSETS
T2.2.5 WORKING IN SECURE AREAS
T2.2.6 PUBLIC ACCESS, DELIVERY, AND LOADING AREAS
T2.3.4 EQUIPMENT MAINTENANCE
T2.3.5 SECURITY OF EQUIPMENT OFF-PREMISES
T2.3.6 SECURE DISPOSAL OR RE-USE OF EQUIPMENT
T2.3.7 REMOVAL OF PROPERTY
T2.3.9 CLEAR DESK AND CLEAR SCREEN POLICY
T3.2.2 DOCUMENTED OPERATING PROCEDURES
T3.3.2 SYSTEM ACCEPTANCE AND TESTING
T3.6.1 MONITORING POLICY AND PROCEDURES
T3.6.6 FAULT LOGGING
T4.1.1 COMMUNICATIONS POLICY
T4.2.2 AGREEMENTS ON INFORMATION TRANSFER
T4.2.3 PHYSICAL MEDIA IN TRANSIT
T4.2.4 ELECTRONIC MESSAGING
T4.3.2 ON-LINE TRANSACTIONS
T5.4.6 NETWORK ROUTING CONTROL
T5.6.3 PUBLICLY ACCESSIBLE CONTENT
T7.2.1 SECURITY REQUIREMENTS ANALYSIS AND SPECIFICATION
T7.5.2 PROTECTION OF SYSTEM TEST DATA
T7.5.3 ACCESS CONTROL TO PROGRAM SOURCE CODE
T7.6.1 CHANGE CONTROL PROCEDURES
T7.6.2 TECHNICAL REVIEW OF APPLICATIONS AFTER OPERATING SYSTEM CHANGES
T7.6.5 OUTSOURCED SOFTWARE DEVELOPMENT
T7.8.6 PROCESSES TO ADDRESS WEAKNESSES OR DEFICIENCIES
T9.2.1 DEVELOPING INFORMATION SYSTEMS CONTINUITY PLANS
T9.2.2 IMPLEMENTING INFORMATION SYSTEMS CONTINUITY PLANS
T9.3.1 TESTING, MAINTAINING AND RE-ASSESSING INFORMATION SYSTEMS CONTINUITY PLANS

--- Page 259 ---

# CONTROL CONTROL <br> NUMBER NAME 

## P4 CONTROLS

M1.3.3 CONTACT WITH AUTHORITIES
M1.3.4 CONTACT WITH SPECIAL INTEREST GROUPS
M5.2.2 INTELLECTUAL PROPERTY RIGHTS (IPR)
M5.2.7 LIABILITY TO THE INFORMATION SHARING COMMUNITY
M5.3.1 COMPLIANCE WITH SECURITY POLICIES AND STANDARDS
M5.5.1 INFORMATION SYSTEMS AUDIT CONTROLS
M5.5.2 PROTECTION OF INFORMATION SYSTEMS AUDIT TOOLS
M5.5.3 AUDIT OF COMMUNITY FUNCTIONS

T2.1.1 PHYSICAL AND ENVIRONMENTAL SECURITY POLICY
T2.2.4 PROTECTING AGAINST EXTERNAL AND ENVIRONMENTAL THREATS
T2.3.2 SUPPORTING UTILITIES
T2.3.3 CABLING SECURITY
T3.1.1 OPERATIONS MANAGEMENT POLICY
T3.2.3 CHANGE MANAGEMENT
T3.3.1 CAPACITY MANAGEMENT
T3.6.7 CLOCK SYNCHRONIZATION
T4.2.5 BUSINESS INFORMATION SYSTEMS
T4.3.3 PUBLICLY AVAILABLE INFORMATION
T4.4.1 CONNECTIVITY TO INFORMATION SHARING PLATFORMS
T4.4.2 INFORMATION RELEASED INTO INFORMATION SHARING COMMUNITIES
T5.4.4 REMOTE DIAGNOSTIC AND CONFIGURATION PROTECTION
T5.5.4 USE OF SYSTEM UTILITIES
T5.7.1 ACCESS CONTROL FOR MOBILE DEVICES
T5.7.2 TELEWORKING
T6.1.1 THIRD PARTY SECURITY POLICY
T7.1.1 INFORMATION SYSTEMS ACQUISITION, DEVELOPMENT AND MAINTENANCE POLICY
T7.2.2 DEVELOPER-PROVIDED TRAINING
T7.5.1 CONTROL OF OPERATIONAL SOFTWARE
T7.8.1 SUPPLY CHAIN PROTECTION STRATEGY
T7.8.2 SUPPLIER REVIEWS
T7.8.3 LIMITATION OF HARM
T7.8.4 SUPPLY CHAIN OPERATIONS SECURITY
T7.8.5 RELIABLE DELIVERY

--- Page 260 ---

# CONTROL CONTROL NUMBER NAME 

T7.8.7 SUPPLY OF CRITICAL INFORMATION SYSTEM COMPONENTS
T8.2.3 INCIDENT CLASSIFICATION
T8.2.4 INCIDENT RESPONSE TRAINING
T8.2.5 INCIDENT RESPONSE TESTING
T8.2.6 INCIDENT RESPONSE ASSISTANCE
T8.2.7 INFORMATION SECURITY INCIDENT DOCUMENTATION
T8.2.8 LEARNING FROM INFORMATION SECURITY INCIDENTS
T8.2.9 COLLECTION OF EVIDENCE
T8.3.1 SITUATIONAL AWARENESS
T8.3.2 REPORTING INFORMATION SECURITY EVENTS
T8.3.3 REPORTING SECURITY WEAKNESSES
T9.1.1 INFORMATION SYSTEMS CONTINUITY PLANNING POLICY

--- Page 261 ---

# ANNEX C 

## MAPPING OF CONTROLS AGAINST LEADING STANDARDS

The following table provides a list of the UAE IA Standards security controls mapping against the security controls of ISO 27001, NIST Special Publication 800-53, SANS 20 and ADSIC Information Security Standards. This mapping enables the implementing entities to compare the requirements of the UAE IA Standards against other leading standards.

TABLE 8: MAPPING OFUAEIA STANDARDS CONTROLS AGAINST LEADING STANDARDS

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800- <br> 53r4 | ADSIC <br> v1.0 | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M1.1.1 | Understanding the Entity and its Context | NONE | NONE | NONE | NONE |
| M1.1.2 | Leadership and Management Commitment | A5.1.1, |  |  |  |
| A.6.1.2 | $\begin{aligned} & \text { XX-1 controls, } \\ & \text { PM-1, IR-4, PL-2, } \\ & \text { CP-2, CP-4, IR-4, } \\ & \text { PL-1, PL-6, PM-2, } \\ & \text { SA-2; SP 800-39, SP } \\ & 800-37 \end{aligned}$ | 1.2.1 | NONE |  |  |
| M1.1.3 | Roles and Responsibilities for Information Security | A6.1.3 | XX-1 controls, AC-5, AC-6, CM-9. PM-2; SP 800-39, SP 800-37 | 1.2.1 | NONE |
| M1.2.1 | Information Security Policy | A.5.1.1 | XX-1 Controls, <br> PM-1 | $\begin{aligned} & \text { 2.1.1, } \\ & \text { 2.1.2 } \end{aligned}$ | SG. 8 |
| M1.2.2 | Supporting Policies for Information Security | NONE | XX-1 controls, CA-2, CA-7, RA-5, AU-1, AU-2, SI-4, AU-9 | NONE | SG. 8 |
| M1.3.1 | Authorization <br> Process for <br> Information <br> Systems | A.6.1.4 | $\begin{aligned} & \text { PM-10, CA-1, } \\ & \text { CA-6; SP 800- } \\ & 37 \end{aligned}$ | 3.3.1 | IS. 13 |

--- Page 262 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M1.3.2 | Confidentiality Agreements | A.6.1.5 | $\begin{aligned} & \text { PL-4, PS-6, } \\ & \text { SA-9 } \end{aligned}$ | 8.1.1 | HR. 1 |
| M1.3.3 | Contact W with Authorities | A.6.1.6 | $\begin{aligned} & \text { IR-4, IR-6, } \\ & \text { IR-7, PE-13, } \\ & \text { SA-19, SI-5 } \end{aligned}$ | 13.1.1 | IM. 5 |
| M1.3.4 | Contact W with Special Interest Groups | A.6.1.7 | PM-15, SI-5 | 13.2.2 | TA. 5 |
| M1.3.5 | Identification of Risks Related to External Parties | A.6.2.1 | PM-9, AC-20, CA-3, RA-3, SA-9 | NONE | RM. 2 |
| M1.3.6 | Addressing Security When Dealing W with Customers | A.6.2.2 | $\begin{aligned} & \text { AC-8, AT-2, } \\ & \text { AT-3, CA-2, } \\ & \text { CA-3, PL-4, } \\ & \text { SA-9 } \end{aligned}$ | NONE | NONE |
| M1.3.7 | Addressing Security in Third Party Agreements | A.6.2.3 | $\begin{aligned} & \text { CA-3, PL-4, } \\ & \text { PS-6, PS-7, } \\ & \text { SA-9 } \end{aligned}$ | NONE | TP. 2 |
| M1.4.1 | Resources | 5.2.1, |  |  |  |
| A.6.1.2, <br> A.10.3.1 | $\begin{aligned} & \text { XX-1 controls, PM- } \\ & \text { 1, PM-2, CP-2, CP-4, } \\ & \text { IR-4, PL-1, PL-2, } \\ & \text { SA-2 } \end{aligned}$ | NONE | SG.1.9 |  |  |
| M1.4.2 | Internal and External Communication | NONE | NONE | $\begin{aligned} & \text { 5.1.1, } \\ & \text { 5.1.2, } \\ & \text { 5.2.1, } \\ & \text { 5.2.2 } \end{aligned}$ | TA.3, TA. 6 |
| M1.4.3 | Documentation | 4.3 | NONE | NONE | NONE |
| M2.1.1 | Information Security Risk Management Policy | NONE | RA-1, PM-9 | None | NONE |
| M2.2.1 | Information Security Risk Identification | 4.2.1 | RA-2 | 1.3.1 | RM. 2 |

--- Page 263 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M2.2.2 | Information Security Risk Analysis | 4.2.1 | RA-3 | 3.1.1 | RM. 3 |
| M2.2.3 | Information Security Risk Evaluation | 4.2.1 | NONE | 3.1.1 | RM. 3 |
| M1.4.3 | Documentation | 4.3 | NONE | NONE | NONE |
| M2.1.1 | Information Security Risk Management Policy | NONE | RA-1, PM-9 | None | NONE |
| M2.2.1 | Information Security Risk Identification | 4.2.1 | RA-2 | 1.3.1 | RM. 2 |
| M2.2.2 | Information Security Risk Analysis | 4.2.1 | RA-3 | 3.1.1 | RM. 3 |
| M2.2.3 | Information Security Risk Evaluation | 4.2.1 | NONE | 3.1.1 | RM. 3 |
| M2.3.1 | Information Security Risk Treatment Options | 4.2.1 | NONE | $\begin{gathered} \text { RM- } \\ 3.1 .2 \end{gathered}$ | RM. 4 |
| M2.3.2 | Identification of Controls | 4.2.1 | NONE | NONE | RM. 4 |
| M2.3.3 | Risk Treatment Plan | 4.2.1 | NONE | NONE | RM. 4 |
| M2.3.4 | Statement of Applicability | 4.2.1 | NONE | 3.3 | NONE |
| M2.3.5 | Information Security Objectives | NONE | NONE | NONE | NONE |
| M2.4.1 | Information Security Risk Assessment Review and Update | 4.2.3 | RA-3 | NONE | NONE |
| M2.4.2 | Risk Communication and Consultation | NONE | NONE | - | RM.2.2 |
| M3.1.1 | Awareness and Training Policy | NONE | AT-1 | NONE | NONE |
| M3.2.1 | Awareness and Training Program | 5.2.2 | NONE | 4.2.1 | TA. 4 |
| M3.3.1 | Training Needs | 5.2.2 | NONE | 4.2.1 | TA. 4 |

--- Page 264 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M3.3.2 | Implementation Plan | NONE | NONE | 4.2.1 | TA. 4 |
| M3.3.4 | Training Results | NONE | NONE | NONE | NONE |
| M3.3.3 | Training Execution | 5.2.2 | AT-3 | 4.2.2 | TA. 4 |
| M3.3.5 | Records Documentation | 5.2.2 | AT-4 | 4.2.3 | TA. 4 |
| M3.4.1 | Awareness Campaign | NONE | AT-2 | $\begin{aligned} & \text { 4.1.1, } \\ & \text { 4.1.1 } \end{aligned}$ | TA. 2 |
| M4.1.1 | Human Resources Security Policy | NONE | NONE | NONE | NONE |
| M4.2.1 | Screening | A.8.1.2 | PS-3 | 8.1.2 | HR. 2 |
| M4.2.2 | Terms and Conditions of Employment | A.8.1.3 | $\begin{aligned} & \text { AC-20, PL-4, } \\ & \text { PS-6, PS-7 } \end{aligned}$ | 8.1.3 | HR. 3 |
| M4.3.1 | Management Responsibilities | A.8.2.1 | $\begin{aligned} & \text { PL-4, PS-6, } \\ & \text { PS-7, SA-9 } \end{aligned}$ | 8.2.1 | HR. 1 |
| M4.3.2 | Disciplinary Process | A.8.2.3 | PS-8 | 8.2.2 | HR. 5 |
| M4.4.1 | Termination Responsibilities | A.8.3.1 | PS-4, PS-5 | 8.3.1 | HR. 6 |
| M4.4.2 | Return of Assets | A.8.3.2 | PS-4, PS-5 | 8.3.2 | HR. 6 |
| M4.4.3 | Removal of Access Rights | A.8.3.3 | $\begin{aligned} & \text { AC-2, PS-4, } \\ & \text { PS-5 } \end{aligned}$ | 8.3.3 | HR. 6 |
| M5.1.1 | Compliance Policy | NONE | NONE | NONE | NONE |
| M5.2.1 | Identification of Applicable Legislation | A.15.1.1 | $\begin{aligned} & \text { XX-1 controls, } \\ & \text { IA-7 } \end{aligned}$ | 1.3.3 | SG. 5 |
| M5.2.2 | Intellectual Property Rights (IPR) | A.15.1.2 | SA-6 | 1.3.3 | SG. 5 |
| M5.2.3 | Protection of Organizational Records | A.15.1.3 | $\begin{aligned} & \text { AU-9, AU-11, } \\ & \text { CP-9, MP-1, } \\ & \text { MP-4, SA-5, } \\ & \text { SI-12 } \end{aligned}$ | 1.3.3 | SG. 5 |

--- Page 265 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M5.2.4 | Data Protection and Privacy of Personal Information | A.15.1.4 | PL-5;SI-12 | 1.3.3 | SG. 5 |
| M5.2.5 | Prevention of Misuse of Information Systems | A.15.1.5 | $\begin{aligned} & \text { AC-8, AU-6, } \\ & \text { PL-4, PS-6, } \\ & \text { PS-8, SA-7 } \end{aligned}$ | 11.5.1 | NONE |
| M5.2.6 | Regulation of Cryptographic Controls | A.15.1.6 | IA-7, SC-13 | 12.3.1 | IS. 5 |
| M5.2.7 | Liability to the Information Sharing Community | NONE | NONE | NONE | NONE |
| M5.3.1 | Compliance with Security Policies and Standards | A.15.2.1 | $\begin{aligned} & \text { XX-1 controls, } \\ & \text { AC-2, CA-2, } \\ & \text { CA-7, IA-7, } \\ & \text { PE-8, SI-12 } \end{aligned}$ | $\begin{aligned} & 1.3 .4, \\ & 2.0, \\ & 3.4 .1, \\ & 6.2 .1, \\ & 6.2 .2, \\ & 6.2 .3, \\ & 6.3 .1, \\ & 6.3 .2, \\ & 6.3 .3 \end{aligned}$ | IS.1, SG.1, SG.8, SG.9, SG. 10 |
| M5.4.1 | Technical Compliance Checking | A.15.2.2 | $\begin{aligned} & \text { CA-2, CA-7, } \\ & \text { RA-5 } \end{aligned}$ | $\begin{aligned} & 3.2 .1, \\ & 3.4 .1, \\ & 6.3 .1, \\ & 6.3 .2, \\ & 6.3 .3 \end{aligned}$ | IS.13, SG.9, SG. 10 |
| M5.5.1 | Information Systems Audit Controls | A.15.3.1 | $\begin{aligned} & \text { AU-1, AU-2, } \\ & \text { PL-6 } \end{aligned}$ | NONE | SG. 10 |
| M5.5.2 | Protection of Information Systems Audit Tools | A.15.3.2 | AU-9 | 11.5.4 | OM. 13 |
| M5.5.3 | Audit of Community Functions | NONE | NONE | NONE | NONE |
| M6.1.1 | Performance Evaluation Policy | NONE | NONE | NONE | NONE |
| M6.2.1 | Monitoring, Measurement, Analysis and Evaluation | 4.2.2 d) | PM-6 | $\begin{aligned} & 6.2 .2, \\ & 6.2 .3 \end{aligned}$ | SG. 9 |
| M6.2.2 | Internal Audits | 6, A.6.1.8 | $\begin{aligned} & \text { CA-2, CA-7; } \\ & \text { SP 800-39, SP } \\ & 800-37 \end{aligned}$ | 3.2.1 | IS.13, SG. 10 |

--- Page 266 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| M6.3.1 | Corrective Action | 8.1 | NONE | NONE | SG. 1 |
| M6.3.2 | Continual Improvement | 8.2 | NONE | 6.2.3 | SG.1, SG. 10 |
| T1.1.1 | Asset Management Policy | NONE | NONE | NONE | NONE |
| T1.2.1 | Inventory of Assets | A.7.1.1 | $\begin{aligned} & \text { CM-8, CM-9, } \\ & \text { PM-5 } \end{aligned}$ | 7.1.1 | AM. 1 |
| T1.2.2 | Ownership of Assets | A.7.1.2 | $\begin{aligned} & \text { CM-8, CM-9, } \\ & \text { PM-5 } \end{aligned}$ | 7.1.2 | AM. 2 |
| T1.2.3 | Acceptable Use of Assets | A.7.1.3 | AC-20, PL-4 | 7.1.3 | HR. 3 |
| T1.2.4 | Acceptable Bring Your Own Device (BYOD) Arrangements | NONE | NONE | NONE | NONE |
| T1.3.1 | Classification of Information | A.7.2.1 | RA-2 | 7.2.1 | AM. 3 |
| T1.3.2 | Labeling of Information | A.7.2.2 | $\begin{aligned} & \text { AC-16, MP-2, } \\ & \text { MP-3, SC-16 } \end{aligned}$ | 7.2.2 | AM. 4 |
| T1.3.3 | Handling of Information Assets | A.7.2.2 | $\begin{aligned} & \text { AC-16, MP-2, } \\ & \text { MP-3, SC-16 } \end{aligned}$ | 7.2.2 | AM. 4 |
| T1.4.1 | Management of Removable Media | A.10.7.1 | MP Family, PE-16 | 10.7.1 | OM. 16 |
| T1.4.2 | Disposal of Media | A.10.7.2 | MP-6 | 10.7.2 | OM. 16 |
| T2.1.1 | Physical and Environmental Security Policy | NONE | PE-1 | NONE | NONE |
| T2.2.1 | Physical Security Perimeter | A.9.1.1 | PE-3 | 9.1.1 | PE. 2 |
| T2.2.2 | Physical Entry Controls | A.9.1.2 | $\begin{aligned} & \text { PE-3, PE-5, PE- } \\ & \text { 6, PE-7 } \end{aligned}$ | $\begin{aligned} & 9.1 .2, \\ & 9.1 .3 \end{aligned}$ | PE. 2 |
| T2.2.3 | Securing Offices, Rooms and Facilities | A.9.1.3 | PE-3, PE-4, PE-5 | 9.1.4 | PE. 2 |
| T2.2.4 | Protecting Against External and Environmental Threats | A.9.1.4 | CP Family; PE-1, PE-9, PE-10, PE-11, PE-13, PE-15 | 9.1.5 | PE. 2 |

--- Page 267 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T2.2.5 | Working in Secure Areas | A.9.1.5 | AT-2, AT-3 <br> , PL-4,PS-6, <br> PE-2, PE-3, <br> PE-4, PE-6, <br> PE-7, PE-8 | 9.1.6 | PE. 3 |
| T2.2.6 | Public Access, Delivery, and Loading Areas | A.9.1.6 | $\begin{aligned} & \text { PE-3,PE-7, } \\ & \text { PE-16 } \end{aligned}$ | 9.1.7 | PE. 2 |
| T2.3.1 | Equipment Siting and Protection | A.9.2.1 | PE-1, PE-18 | 9.2.1 | PE. 2 |
| T1.3.2 | Labeling of Information | A.7.2.2 | $\begin{aligned} & \text { AC-16, MP-2, } \\ & \text { MP-3, SC-16 } \end{aligned}$ | 7.2.2 | AM. 4 |
| T1.3.3 | Handling of Information Assets | A.7.2.2 | $\begin{aligned} & \text { AC-16, MP-2, } \\ & \text { MP-3, SC-16 } \end{aligned}$ | 7.2.2 | AM. 4 |
| T1.4.1 | Management of Removable Media | A.10.7.1 | MP Family, <br> PE-16 | 10.7.1 | OM. 16 |
| T1.4.2 | Disposal of Media | A.10.7.2 | MP-6 | 10.7.2 | OM. 16 |
| T2.1.1 | Physical and Environmental Security Policy | NONE | PE-1 | NONE | NONE |
| T2.2.1 | Physical Security Perimeter | A.9.1.1 | PE-3 | 9.1.1 | PE. 2 |
| T2.2.2 | Physical Entry Controls | A.9.1.2 | $\begin{aligned} & \text { PE-3,PE-5, } \\ & \text { PE-6,PE-7 } \end{aligned}$ | $\begin{aligned} & \text { 9.1.2, } \\ & \text { 9.1.3 } \end{aligned}$ | PE. 2 |
| T2.2.3 | Securing Offices, Rooms and Facilities | A.9.1.3 | $\begin{aligned} & \text { PE-3,PE-4, } \\ & \text { PE-5 } \end{aligned}$ | 9.1.4 | PE. 2 |
| T2.2.4 | Protecting Against External and Environmental Threats | A.9.1.4 | CP Family; PE-1, PE-9, PE-10, PE-11, PE-13, PE-15 | 9.1.5 | PE. 2 |
| T2.2.5 | Working in Secure Areas | A.9.1.5 | AT-2, AT-3 <br> , PL-4,PS-6, <br> PE-2,PE-3, <br> PE-4,PE-6, <br> PE-7,PE-8 | 9.1.6 | PE. 3 |
| T2.2.6 | Public Access, Delivery, and Loading Areas | A.9.1.6 | $\begin{aligned} & \text { PE-3,PE-7, } \\ & \text { PE-16 } \end{aligned}$ | 9.1.7 | PE. 2 |

--- Page 268 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T2.3.1 | Equipment Siting and Protection | A.9.2.1 | PE-1, PE-18 | 9.2.1 | PE. 2 |
| T2.3.2 | Supporting Utilities | A.9.2.2 | $\begin{aligned} & \text { PE-1, PE-9, } \\ & \text { PE-11, PE-12, } \\ & \text { PE-14 } \end{aligned}$ | 9.2.2 | PE. 2 |
| T2.3.3 | Cabling Security | A.9.2.3 | PE-4, PE-9 | 9.2.3 | NONE |
| T2.3.4 | Equipment Maintenance | A.9.2.4 | MA Family | 9.2.4 | OM. 21 |
| T2.3.5 | Security of Equipment Off-Premises | A.9.2.5 | MP-5, PE-17 | 9.2.5 | PE. 2 |
| T2.3.6 | Secure Disposal or ReUse of Equipment | A.9.2.6 | MP-6 | 9.2.6 | OM. 22 |
| T2.3.7 | Removal of Property | A.9.2.7 | MP-5, PE-16 | 9.2.7 | PE. 2 |
| T2.3.8 | Unattended User Equipment | A.11.3.2 | $\begin{aligned} & \text { AC-11, IA-2, PE- } \\ & \text { 3, PE-5, PE-18, } \\ & \text { SC-10 } \end{aligned}$ | 11.3.2 | PE. 3 |
| T2.3.9 | Clear Desk and Clear Screen Policy | A.11.3.3 | AC-11 | 11.3.3 | PE. 3 |
| T3.1.1 | Operations <br> Management Policy | NONE | CM-1 | 10.1.1 | NONE |
| T3.2.1 | Common Systems Configuration Guidelines | NONE | CM-6 | 12.1.2 | IS. 3 |
| T3.2.2 | Documented Operating Procedures | A.10.1.1 | $\mathrm{XX}-1$ controls, CM-9 | 10.1.1 | OM. 1 |
| T3.2.3 | Change Management | A.10.1.2 | $\begin{aligned} & \text { CM-1, CM-3, } \\ & \text { CM-4, CM-5, } \\ & \text { CM-9 } \end{aligned}$ | 10.1.2 | OM. 2 |
| T3.2.4 | Segregation of Duties | A.10.1.3 | AC-5 | 10.1.3 | HR. 4 |
| T3.2.5 | Separation of Development, Test and Operational Facilities | A.10.1.4 | CM-2 | 10.1.4 | OM. 3 |
| T3.3.1 | Capacity Management | A.10.3.1 | $\begin{aligned} & \text { AU-4, AU-5, CP- } \\ & \text { 2, SA-2, SC-5 } \end{aligned}$ | 10.3.1 | IS. 2 |

--- Page 269 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T3.3.2 | System Acceptance and Testing | A.10.3.2 | CA-2, CA-6, <br> CM-3, CM-4, <br> CM-9, SA-11 | 10.3.2 | OM. 4 |
| T3.4.1 | Controls Against Malware | A.10.4.1 | $\begin{aligned} & \text { AC-19, AT-2, } \\ & \text { SA-8, SC-2, } \\ & \text { SC-3, SC-7, } \\ & \text { SC-14, SI-3, } \\ & \text { SI-7 } \end{aligned}$ | 10.4.1 | OM. 6 |
| T3.5.1 | Information Backup | A.10.5.1 | CP-9 | 10.5.1 | OM. 8 |
| T3.6.1 | Monitoring Policy and Procedures | NONE | AU -1 | 10.10.1 | OM. 5 |
| T3.6.2 | Audit Logging | A.10.10.1 | $\begin{aligned} & \text { AU-1, AU-2, } \\ & \text { AU-3, AU-4, } \\ & \text { AU-5, AU-8, } \\ & \text { AU-11, AU-12 } \end{aligned}$ | 10.10.2 | OM. 20 |
| T3.6.3 | Monitoring System Use | A.10.10.2 | $\begin{aligned} & \text { AU-1, AU-6, } \\ & \text { AU-7, PE-6, } \\ & \text { PE-8, SC-7, } \\ & \text { SI-4 } \end{aligned}$ | 10.10.3 | OM. 20 |
| T3.6.4 | Protection of Log Information | A.10.10.3 | AU-9 | 10.10.4 | OM. 20 |
| T3.6.5 | Administrator and Operator Logs | A.10.10.4 | AU-2, AU-12 | 10.10.5 | OM. 20 |
| T3.6.6 | Fault Logging | A.10.10.5 | $\begin{aligned} & \text { AU-2, AU-6, } \\ & \text { AU-12, SI-2 } \end{aligned}$ | 10.10.6 | OM. 20 |
| T3.6.7 | Clock Synchronization | A.10.10.6 | AU-8 | 10.10.7 | OM. 20 |
| T4.1.1 | Communications Policy | NONE | SC-1 | 10.8.1 | SG. 6 |
| T4.2.1 | Information <br> Transfer Procedures | A.10.8.1 | $\begin{aligned} & \text { AC-1, AC-3, } \\ & \text { AC-4, AC-17, } \\ & \text { AC-18, AC-20, } \\ & \text { CA-3, PL-4, } \\ & \text { PS-6, SC-7, } \\ & \text { SC-16, SI-9 } \end{aligned}$ | 10.8.1 | SG. 6 |
| T4.2.2 | Agreements on Information Transfer | A.10.8.2 | CA-3, SA-9 | 10.8.2 | SG. 6 |

--- Page 270 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T4.2.3 | Physical Media in Transit | A.10.8.3 | MP-5 | 10.8 .3 | OM. 19 |
| T4.2.4 | Electronic <br> Messaging | A.10.8.4 | Multiple controls; electronic messaging not addressed separately in SP 800-53 | 10.8 .4 | OM. 14 |
| T4.2.5 | Business <br> Information <br> Systems | A.10.8.5 | CA-1, CA-3 | 10.8 .5 | NONE |
| T4.3.1 | Electronic Commerce | A.10.9.1 | $\begin{aligned} & \text { AU-10, IA-8, } \\ & \text { SC-7, SC-8, } \\ & \text { SC-9, SC-3, } \\ & \text { SC-14 } \end{aligned}$ | 10.9 .1 | NONE |
| T4.3.2 | On-Line <br> Transactions | A.10.9.2 | $\begin{aligned} & \text { SC-3, SC-7, } \\ & \text { SC-8, SC-9, } \\ & \text { SC-14 } \end{aligned}$ | 10.9 .2 | NONE |
| T4.3.3 | Publicly Available Information | A.10.9.3 | SC-14 | 10.9 .3 | NONE |
| T4.4.1 | Connectivity to Information Sharing Platforms | NONE | NONE | NONE | NONE |
| T4.4.2 | Information <br> Released into <br> Information Sharing Communities | NONE | NONE | NONE | NONE |
| T4.5.1 | Network Controls | A.10.6.1 | $\begin{aligned} & \text { AC-4, AC-17, } \\ & \text { AC-18, AC-20, } \\ & \text { CA-3, CP-8, } \\ & \text { PE-5, SC-7, } \\ & \text { SC-8, SC-9, } \\ & \text { SC-10, SC-19, } \\ & \text { SC-20, SC-21, } \\ & \text { SC-22, SC-23 } \end{aligned}$ | 10.6 .1 | IS. 11 |
| T4.5.2 | Security of Network Services | A.10.6.2 | SA-9, SC-8, SC-9 | 10.6 .2 | IS. 11 |
| T4.5.3 | Segregation in Networks | A.11.4.5 | $\begin{aligned} & \text { AC-4, SA-8, } \\ & \text { SC-7 } \end{aligned}$ | 11.4 .5 | IS. 10 |

--- Page 271 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T4.5.4 | Security of Wireless Networks | A.11.4.5 | $\begin{aligned} & \text { AC-4, SA-8, } \\ & \text { SC-7 } \end{aligned}$ | 11.4.5 | IS. 10 |
| T5.1.1 | Access Control Policy | A.11.1.1 | $\begin{aligned} & \text { AC-1, AC-5, } \\ & \text { AC-6, AC-17, } \\ & \text { AC-18, AC-19, } \\ & \text { CM-5, MP-1, } \\ & \text { SI-9 } \end{aligned}$ | 11.1.1 | IA. 4 |
| T5.2.1 | User Registration | A.11.2.1 | $\begin{aligned} & \text { AC-1, AC-2, AC- } \\ & \text { 21, IA-5, PE-1, } \\ & \text { PE-2 } \end{aligned}$ | 11.2.1 | IA. 2 |
| T5.2.2 | Privilege Management | A.11.2.2 | $\begin{aligned} & \text { AC-1, AC-2, AC- } \\ & \text { 6, AC-21, PE-1, } \\ & \text { PE-2, SI-9 } \end{aligned}$ | 11.2.2 | IA. 4 |
| T5.2.3 | User Security Credentials Management | A.11.2.3 | IA-5 | 11.2.3 | IA. 2 |
| T5.2.4 | Review of User Access Rights | A.11.2.4 | AC-2, PE-2 | 11.2.4 | IA. 4 |
| T5.3.1 | Use of Security Credentials | A.11.3.1 | IA-2, IA-5 | 11.3.1 | IA. 3 |
| T5.4.1 | Policy on Use of Network Services | A.11.4.1 | $\begin{aligned} & \text { AC-1, AC-5, AC- } \\ & \text { 6, AC-17, AC-18, } \\ & \text { AC-20 } \end{aligned}$ | 11.4.1 | IA. 4 |
| T5.4.2 | User Authentication for External Connections | A.11.4.2 | $\begin{aligned} & \text { AC-17, AC-18, } \\ & \text { AC-20, CA-3, } \\ & \text { IA-2, IA-8 } \end{aligned}$ | 11.4.2 | IA. 5 |
| T5.4.3 | Equipment <br> Identification in Networks | A.11.4.3 | AC-19, IA-3 | 11.4.3 | OM. 15 |
| T5.4.4 | Remote Diagnostic and Configuration Protection | A.11.4.4 | $\begin{aligned} & \text { AC-3, AC-6, AC- } \\ & \text { 17, AC-18, PE-3, } \\ & \text { MA-3, MA-4 } \end{aligned}$ | 11.4.4 | OM. 12 |
| T5.4.5 | Network Connection Control | A.11.4.6 | $\begin{aligned} & \text { AC-3, AC-6, } \\ & \text { AC-17, AC-18, } \\ & \text { SC-7 } \end{aligned}$ | 11.4.6 | IS. 10 |
| T5.4.6 | Network Routing Control | A.11.4.7 | $\begin{aligned} & \text { AC-4, AC-17, } \\ & \text { AC-18 } \end{aligned}$ | 11.4.7 | IS. 11 |
| T5.4.7 | Wireless Access | A.10.6.1, <br> A.10.8.1, <br> A.11.4.1, <br> A.11.4.2, <br> A.11.4.6, <br> A.11.7.1 | AC-18 | 11.4.2 | IA. 5 |

--- Page 272 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T5.5.1 | Secure Log-oOn Procedures | A.11.5.1 | $\begin{aligned} & \text { AC-7, AC-8, AC- } \\ & \text { 9, AC-10, IA-2, } \\ & \text { IA-6, IA-8, SC10 } \end{aligned}$ | 11.5.1 | IA. 2 |
| T5.5.2 | User Identification and Authentication | A.11.5.2 | IA-2, IA-4, IA-5, IA-8 | 11.5.2 | IA. 1 |
| T5.5.3 | User Credentials Management System | A.11.5.3 | IA-2, IA-5 | 11.5.3 | IA. 3 |
| T5.5.4 | Use of System Utilities | A.11.5.4 | AC-3, AC-6 | 11.5.4 | OM. 13 |
| T5.6.1 | Information Access Restriction | A.11.6.1 | $\begin{aligned} & \text { AC-3, AC-6, AC- } \\ & \text { 14, CM-5 } \end{aligned}$ | 11.6.1 | IA. 4 |
| T5.6.2 | Sensitive System Isolation | A.11.6.2 | SP 800-39 | 11.6.1 | IA. 4 |
| T5.6.3 | Publicly Accessible Content | A.10.9.3 | AC-22, SC-14 | 10.9.3 | NONE |
| T5.7.1 | Access Control for Mobile Devices | A.11.7.1 | $\begin{aligned} & \text { AC-1, AC-17, } \\ & \text { AC-18, AC-19, } \\ & \text { PL-4, PS-6 } \end{aligned}$ | 11.7.1 | IS. 12 |
| T5.7.2 | Teleworking | A.11.7.2 | $\begin{aligned} & \text { AC-1, AC-4, } \\ & \text { AC-17, AC-18, } \\ & \text { PE-17, PL-4, } \\ & \text { PS-6 } \end{aligned}$ | 11.7.2 | IA. 5 |
| T6.1.1 | Third Party Security Policy | NONE | PS-7 | NONE | NONE |
| T6.2.1 | Service Delivery | A.10.2.1 | SA-9 | 10.2.1 | TP. 3 |
| T6.2.2 | Monitoring and Review of Third Party Services | A.10.2.2 | SA-9 | 10.2.2 | TP. 3 |
| T6.2.3 | Managing Changes to Third Party Services | A.10.2.3 | RA-3, SA-9 | NONE | NONE |
| T6.3.1 | Information Security Requirements for Cloud Environments | NONE | NONE | NONE | NONE |
| T6.3.2 | Service Delivery Agreements with Cloud Providers | NONE | NONE | NONE | NONE |
| T7.1.1 | Information Systems Acquisition, Development and Maintenance Policy | NONE | SA-1, MA-1, SI-1 | NONE | NONE |

--- Page 273 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T7.2.1 | Security <br> Requirements <br> Analysis and <br> Specification | A.12.1.1 | SA-1, SA-3, SA-4 | 12.1.1 | IS. 1 |
| T7.2.2 | Developer-Provided Training | NONE | SA-16 | NONE | NONE |
| T7.3.1 | Input Data <br> Validation | A.12.2.1 | SI-9, SI-10 | 12.2.1 | IS. 2 |
| T7.3.2 | Control of Internal Processing | A.12.2.2 | $\begin{aligned} & \text { SI-7, SI-9, } \\ & \text { SI-10 } \end{aligned}$ | 12.2.2 | IS. 2 |
| T7.3.3 | Message Integrity | A.12.2.3 | AU-10, SC-8, SI-7 | 12.2.3 | IS. 2 |
| T7.3.4 | Output Data <br> Validation | A.12.2.4 | No Mapping | 12.2.4 | IS. 2 |
| T7.4.1 | Policy on the Use of Cryptographic Controls | A.12.3.1 | Multiple controls address cryptography (e.g., IA-7, SC-8, SC-9, SC-12, SC-13) | 12.3.1 | IS. 5 |
| T7.4.2 | Key Management | A.12.3.2 | SC-12, SC-17 | 12.3.1 | IS. 5 |
| T7.5.1 | Control of Operational Software | A.12.4.1 | $\begin{aligned} & \text { CM-1, CM-2, } \\ & \text { CM-3, CM-4, } \\ & \text { CM-5, CM-9, } \\ & \text { PL-4, SA-6, } \\ & \text { SA-7 } \end{aligned}$ | 12.4.1 | OM. 1 |
| T7.5.2 | Protection of System Test Data | A.12.4.2 | Multiple controls; protection of test data not addressed separately in SP 800-53 (e.g., AC-3, AC-4) | 12.4.2 | IS. 15 |
| T7.5.3 | Access Control to Program Source Code | A.12.4.3 | $\begin{aligned} & \text { AC-3, AC-6, } \\ & \text { CM-5, CM-9, } \\ & \text { MA-5, SA-10 } \end{aligned}$ | 12.4.3 | IS. 4 |
| T7.6.1 | Change Control Procedures | A.12.5.1 | $\begin{aligned} & \text { CM-1, CM-3, } \\ & \text { CM-9, SA-10 } \end{aligned}$ | 12.5.1 | OM. 2 |

--- Page 274 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T7.6.2 | Technical Review of Applications After Operating System Changes | A.12.5.2 | CM-3, CM-4, CM-9, SI-2 | 12.5.2 | OM. 2 |
| T7.6.3 | Restrictions on Changes to Software Packages | A.12.5.3 | $\begin{aligned} & \text { CM-3, CM-4, } \\ & \text { CM-5, CM-9 } \end{aligned}$ | 12.5.3 | OM. 2 |
| T7.6.4 | Information Leakage | A.12.5.4 | AC-4, PE-19 | 12.5.4 | IS. 6 |
| T7.6.5 | Outsourced <br> Software <br> Development | A.12.5.5 | SA-1, SA-4, SA-6, SA-7, SA-8, SA-9, SA-11, SA-12, SA-13 | 12.5.5 | TP. 2 |
| T7.7.1 | Control of Technical Vulnerabilities | A.12.6.1 | RA-3, RA-5, SI-2, SI-5 | 3.4.1 | OM. 7 |
| T7.8.1 | Supply Chain <br> Protection Strategy | NONE | SA-12 | NONE | NONE |
| T7.8.2 | Supplier Reviews | NONE | SA-12 | NONE | TP. 1 |
| T7.8.3 | Limitation of Harm | NONE | SA-12 | NONE | NONE |
| T7.8.4 | Supply Chain Operations Security | NONE | SA-12 | NONE | NONE |
| T7.8.5 | Reliable Delivery | NONE | SA-12 | NONE | NONE |
| T7.8.6 | Processes <br> to Address <br> Weaknesses or <br> Deficiencies | NONE | SA-12 | NONE | NONE |
| T7.8.7 | Supply of Critical Information System Components | NONE | SA-12 | NONE | NONE |
| T8.1.1 | Information <br> Security Incident <br> Management Policy | NONE | IR-1 | NONE | NONE |
| T8.2.1 | Incident Response Plan | A.13.2.1 | IR-8 | NONE | IM. 4 |
| T8.2.2 | Computer Security Incident Response Team | NONE | Partially (IR10) | NONE | IM. 2 |

--- Page 275 ---

| CONTROL NUMBER | CONTROL NAME | ISO 27001 ISO 27002 | NIST SP800-53r4 | $\begin{aligned} & \text { ADSIC } \\ & \text { v1.0 } \end{aligned}$ | ADSIC v2.0 |
| :--: | :--: | :--: | :--: | :--: | :--: |
| T8.2.3 | Incident Classification | NONE | NONE | NONE | IM. 4 <br> (Partially) |
| T8.2.4 | Incident Response Training | NONE | IR-2 | NONE | NONE |
| T8.2.5 | Incident Response Testing | NONE | IR-3 | 14.1.5 | IM.8.3 |
| T8.2.6 | Incident Response Assistance | NONE | IR-7 | NONE | IM.8.1, |
| IM.8.5 |  |  |  |  |  |
| T8.2.7 | Information <br> Security Incident <br> Documentation | NONE | NONE | NONE | IM. 7 |
| T8.2.8 | Learning From Information Security Incidents | A.13.2.2 | IR-4 | 13.2.3 | NONE |
| T8.2.9 | Collection of Evidence | A.13.2.3 | AU-9, IR-4 | 13.2.4 | IM. 5 |
| T8.3.1 | Situational Awareness | NONE | PM-16 | NONE | IM.6.6 |
| T8.3.2 | Reporting <br> Information Security Events | A.13.1.1 | $\begin{aligned} & \text { AU-6, IR-1, IR- } \\ & 6, \text { SI-4, SI-5 } \end{aligned}$ | 13.1.1 | IM. 3 |
| T8.3.3 | Reporting Security Weaknesses | A.13.1.2 | $\begin{aligned} & \text { PL-4, SI-2, SI- } \\ & 4, \text { SI-5 } \end{aligned}$ | 13.1.2 | IM.3.4 <br> (Partially) |
| T9.1.1 | Information <br> Systems Continuity Planning Policy | NONE | CP-1 | 14.1.1 | IC. 1 |
| T9.2.1 | Developing <br> Information <br> Systems Continuity Plans | A.14.1.3 | CP Family | 14.1.3 | IC. 3 |
| T9.2.2 | Implementing Information Systems Continuity Plans | A.14.1.3 | CP Family | 14.1.3 | IC. 3 |
| T9.3.1 | Testing, Maintaining and Re-Assessing Information Systems Continuity Plans | A.14.1.5 | $\begin{aligned} & \text { CP-2, CP-4, } \\ & \text { CP-5 } \end{aligned}$ | 14.1.5 | IC. 4 |

--- Page 276 ---

# ANNEX D <br> MAPPING OF THREATS TO CONTROLS 

The following table provides examples of typical threats along with their mitigating controls. The list of threats types are aggregated from benchmark risk registers and mapped to mitigating controls to assist implementing entities during their risk assessment process.

Overall, a number of security controls are needed to mitigate specific threat types given the complex nature of the threats. As such, threat types along with their corresponding mitigating controls are outlined in Table 9 below.

## TABLE 9: MAPPING OF THREATS TO CONTROLS

| CATEGORY | THREAT TYPE | CONTROL NUMBERS OF MITIGATING CONTROLS |
| :--: | :--: | :--: |
|  |  | M3.3.3; M4.4.3; T1.4.1; T3.4.1; T3.4.2; T3.6.2; T3.6.3; T3.6.4; T4.5.1; T4.5.3; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.4; T5.4.5; T5.4.6; T5.5.1; T5.5.2; T5.5.3; T5.6.1; T7.7.1 |
|  | Send Data to External Site/Entity | T1.4.1; T4.5.1; T5.4.2; T5.4.5; T5.5.1; T5.5.2; T5.5.3; T6.2.1; T6.2.2; T6.2.3; T6.3.1; T6.3.2 |
|  | Backdoor or Command and Control | M4.4.3; T1.4.1; T1.4.2; T3.4.1; T3.4.2; T3.5.1; T3.6.2; T3.6.3; T3.6.4; T3.6.5; T4.5.1; T4.5.2; T4.5.3; T4.5.4; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.2; T5.4.3; T5.4.5; T5.4.7; T5.5.1; T5.5.2; T5.5.3; T5.6.1; T5.6.2; T7.7.1 |
|  | Disable or interfere with security controls | T2.2.1; T2.2.2; T2.2.3; T2.2.5; T2.2.6; T2.3.8; T3.4.1; T3.4.2; T3.6.2; T5.2.3; T5.2.4; T5.3.1; T5.4.2; T7.3.3; T7.6.2; T7.6.3; T7.7.1 |
| MALWARE | System / Network Utilities | T2.3.2; T3.4.1; T3.4.2; T4.5.1; T4.5.2; T4.5.4; T5.4.7; T5.5.4; T5.6.2 |
|  | RAM Scraper | T2.3.9; T3.4.1; T3.4.2; T3.6.3; T3.6.4; T3.6.5; T4.3.1; T4.3.2; T4.5.2; T5.4.2; T5.5.1; T5.5.2; T7.4.1; T7.4.2; T7.6.4; T7.7.1 |
|  | Data from Untrustworthy Sources | M3.3.3; M3.4.1; T3.4.1; T5.5.2 |
|  | Capture Data Resident on System | T3.2.5; T3.4.1; T3.4.2; T3.6.4; T4.5.3 |
|  | Download/Install additional Malware or Updates | T1.4.1; T3.4.1; T3.4.2; T3.5.1; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T7.5.3; T7.6.3; T7.6.5 |
|  | Redirect to another site/ address | T3.4.1; T3.4.2; T5.4.2 |

--- Page 277 ---

| CATEGORY | THREAT TYPE | CONTROL NUMBERS OF MITIGATING CONTROLS |
| :--: | :--: | :--: |
|  | Exploitation of default or guessable credentials | M1.3.7; T4.5.3; T4.5.4; T5.2.4; T4.4.7; T5.5.1; T5.5.3; T6.1.1; T6.2.2 |
|  | Use of Stolen Login Credentials | M4.4.3; T3.6.2; T3.6.3; T3.6.5; T4.5.1; T4.5.2; T4.5.3; T5.1.1; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.1; T5.4.3; T5.4.5; T5.5.1; T5.5.2; T5.5.3; T5.6.1 |
|  | Brute Force and Dictionary Attacks | T5.1.1; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.2; T5.5.1; T5.5.3 |
|  | Exploitation of backdoor or command and control channels | M4.4.3; T1.4.1; T1.4.2; T3.4.1; T3.4.2; T3.5.1; T3.6.2; T3.6.3; T3.6.4; T3.6.5; T4.5.1; T4.5.2; T4.5.3; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.2; T5.4.3; T5.4.5; T5.5.1; T5.5.2; T5.5.3; T5.6.1; T5.6.2; T7.7.1 |
|  | Authentication Bypass | M5.4.1; T3.5.1; T3.6.3; T3.6.4; T3.6.5; T4.5.1; T4.5.3; T5.4.3; T5.4.5; T5.4.6; T5.5.3; T5.6.1; T7.7.1; T7.8.6 |
| HACKING | SQL Injection | M5.4.1; T1.4.1; T3.2.5; T3.4.1; T3.4.2; T3.5.1; T3.6.3; T3.6.4; T4.5.1; T5.2.2; T5.5.2; T6.3.1; T7.3.1; T7.3.2; T7.3.3; T7.3.4; T7.5.2; T7.7.1; T7.8.6 |
|  | Denial of Service (DOS) or DDOS | T3.2.1; T4.5.2; T4.5.4; T5.4.7; T4.5.3 |
|  | Remote File Inclusion | T3.2.1; T3.4.1; T3.4.2; T4.5.1; T4.5.2; T7.4.1; T7.4.2; T7.7.1 |
|  | Abuse of Functionality | T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.4; T5.4.5; T5.5.1; T5.7.1; T7.3.4; T7.4.1; T7.4.2; T7.6.3; T7.8.3 |
|  | Remote Spying | M4.4.2; M5.2.3; M5.2.4; T3.4.1; T3.4.2; T3.6.1; T3.6.3; T3.6.4; T3.6.5; T4.5.1; T4.5.3; T5.1.1; T5.2.1; T5.2.3; T5.3.1; T5.4.2; T5.4.3; T5.4.5; T5.5.1; T5.5.2; T5.6.1; T5.6.2; T7.4.1; T7.4.2; T7.7.1; T7.8.5 |
|  | Eavesdropping / Packet Sniffing | T2.2.1; T2.2.2; T4.1.1; T4.2.1; T4.2.2; T4.2.3; T4.2.4; T4.3.1; T4.3.2; T4.5.1; T5.4.3; T5.4.6; T7.4.1 |
|  | Pretexting | M3.4.1; M4.1.1; M4.3.1; M4.3.2; T5.1.1; T5.6.1; T5.6.3 |
|  | Intentional Leaks / Sharing of Data by Staff | M3.4.1; M4.1.1; M4.2.1; M4.3.2; M5.2.3; M5.2.4; T3.6.3; T5.1.1; T5.2.2; T5.2.4; T5.4.2; T5.5.2; T5.6.1; T7.6.4 |
|  | Phishing | M3.3.3; M3.4.1; M4.1.1; T3.4.1; T3.4.2; T4.1.1; T4.2.1; T5.1.1; T5.5.1; T5.5.2; T5.5.3 |
| SOCIAL | Accidental Leaks / Sharing of Data by Staff | M3.3.3; M3.4.1; M5.2.3; T3.6.3; T5.1.1; T5.2.2; T5.4.2; T5.5.2; T5.6.1; T5.6.3; T7.6.4 |
|  | Illegal Processing of Data | M3.3.3; M3.4.2; M4.2.1; M4.3.2; M4.4.3; M5.2.2; M5.2.3; M5.2.7; T1.3.1; T1.3.2; T3.2.4; T3.5.1; T3.6.3; T4.2.1; T4.2.4; T5.2.2; T5.2.3; T5.2.4; T5.3.1; T5.4.2; T5.4.3; T5.5.2; T5.5.3; T5.6.1; T5.6.2 |

--- Page 278 ---

| CATEGORY | THREAT TYPE | CONTROL NUMBERS OF MITIGATING CONTROLS |
| :--: | :--: | :--: |
|  | Embezzlement, <br> Skimming, and Related <br> Fraud | T1.2.2; T1.2.3; T1.3.2; T1.4.1; T1.4.2 |
|  | Use of Unapproved Hardware/Devices | M1.3.1; M1.3.6; M1.1.3; M5.2.5; T1.1.1; T1.2.1; T1.2.2; T1.2.3; T1.3.3; T2.3.4; T3.2.4; T3.3.2; T3.6.3; T5.4.3; T7.7.1 |
|  | Abuse of System Access/ Privileges | M4.4.1; M4.4.3; T3.2.4; T4.5.1; T4.5.3; T5.2.1; T5.2.2; T5.2.3; T5.2.4; T5.5.2; T7.6.4 |
|  | Retrieval of Recycled or Discarded Media | M4.4.2; T1.1.1; T1.2.1; T1.4.1; T1.4.2; T2.3.6; T3.4.1; T3.4.2 |
|  | Equipment Failure | T2.3.1; T2.3.4; T3.2.1; T3.2.4; T3.3.2; T3.5.1; T3.6.2; T3.6.3; T3.6.6; T3.6.7; T5.4.3; T7.3.1; T7.3.2; T7.3.4; T9.2.1; T9.2.2; T9.3.1 |
|  | Equipment Malfunction | M3.3.2; M3.3.3; M5.2.5; T1.2.2; T1.3.3; T3.2.1; T3.2.2; T3.2.4; T3.3.2; T3.5.1; T3.6.2; T3.6.3; T3.6.6; T3.6.7; T5.4.3; T7.7.1; T9.2.1; T9.2.2; T9.3.1 |
|  | Software Malfunction | M3.3.2; M3.3.3; T1.2.2; T3.2.1; T3.2.2; T3.2.4; T3.3.2; T3.5.1; T3.6.2; T3.6.3; T3.6.6; T7.2.2; T7.3.1; T7.3.2; T7.3.4; T7.5.1; T7.5.3; T7.6.2; T7.6.3; T7.6.5; T7.7.1; T9.2.1; T9.2.2; T9.3.1 |
|  | Error in Use | M3.3.1; M3.3.2; M3.3.3; M3.4.1; M5.2.5; T3.2.2; T3.5.1; T3.6.3; T3.6.6 |
|  | Use of Counterfeit or Copied Software | T1.2.2; T3.2.4; T3.2.5; T3.3.2; T7.3.1; T7.3.2; T7.3.4; T7.5.1; T7.6.3; T7.6.5 |
|  | Misappropriation of Private Knowledge | M3.3.2; M3.3.3; M3.4.1; T1.3.1; T1.3.2; T1.4.1; T1.4.2; T2.2.1; T2.2.2; T2.2.3; T2.2.5; T2.2.6; T2.3.6; T2.3.8; T4.2.3; T4.3.1; T4.3.3; T4.4.1; T4.4.2; T5.2.2; T5.2.3; T5.2.4; T5.7.1; T5.7.2 |
|  | Inappropriate Web/ <br> Internet Usage | M3.4.1; T3.4.1; T4.3.1; T4.3.2; T4.5.1; T4.5.2; T5.2.2; T5.4.2 |
| PHYSICAL | Tampering | M3.2.1; M3.3.1; M3.4.1; M5.4.1; T2.2.3; T2.3.1; T2.3.4; T2.3.5; T2.3.8; T3.4.1; T3.4.2; T3.5.1; T3.6.3; T3.6.5; T5.2.3; T5.4.2; T5.4.4; T5.5.2; T7.5.3; T7.6.2; T7.6.3; T7.7.1 |
|  | Major Accident | T2.1.1; T2.2.3; T2.2.4; T2.3.1; T3.5.1; T8.1.1; T8.3.2; T8.2.1; T8.2.2; T8.3.1; T8.2.3; T8.2.4; T8.2.5; T8.2.7; T9.1.1; T9.2.1; T9.2.2; T9.3.1 |
|  | Destruction of Equipment or Media | T1.1.1; T1.2.2; T1.2.3; T1.4.1; T2.1.1; T2.2.1; T2.2.2; T2.2.3; T2.3.1; T2.3.5; T2.3.8; T3.2.4; T3.5.1; T9.1.1; T9.2.1; T9.2.2; T9.3.1 |
|  | Physical Theft of Asset <br> - Including Document, <br> Media and Equipment | M3.3.3; M3.4.1; M4.3.2; M4.4.2; T1.1.1; T1.2.1; T1.2.2; T1.4.1; T1.4.2; T2.2.1; T2.2.2; T2.2.3; T2.3.1; T2.3.7; T2.3.8; T2.3.9; T3.5.1; T5.6.2; T7.4.1; T7.4.2 |
|  | Unauthorized Use of Equipment | M1.3.1; M4.4.1; M5.2.5; T1.2.2; T2.3.1; T2.3.5; T3.2.4; T3.6.3; T5.2.3; T5.3.1; T5.5.2 |
|  | Corruption of Data | T3.5.1; T4.2.3; T4.2.4; T4.5.3; T7.3.2; T7.3.3; T7.3.4 |

--- Page 279 ---

# ANNEXE SECTOR AND NATIONAL LEVEL CONTROLS 

The following table provides a list of the sector and national level security controls. As a recap, sector and national level controls are designed to overcome the silos created by a single-entity approach to IA, and hence create a stronger and more integrated approach for national information assurance. They serve as foundational elements for developing the sector and national views of IA by enabling the integration and analysis of information relating to security threats, risks and incidents, as well as the state of these Standards implementation and risk assessment outcomes.

Overall, the UAE IA Standards provides a total of 15 sector and national level controls as outlined in Table 10 below.

## TABLE 10: SECTOR AND NATIONAL LEVEL CONTROLS

## CONTROL NUMBER

## M1

M1.3
M1.3.3
M1.3.4

## M5

M5.1
M5.1.1

T3
T3.6
T3.6.1

## CONTROL

NAME

## STRATEGY AND PLANNING ORGANIZATION OF INFORMATION SECURITY

Contact with Authorities
Contact with Special Interest Groups

## COMPLIANCE

## COMPLIANCE POLICY

Compliance Policy

## OPERATIONS MANAGEMENT

## MONITORING

Monitoring Policy and Procedures

--- Page 280 ---

| T4 | COMMUNICATIONS |
| :-- | :-- |
| T4.4 | INFORMATION EXCHANGES PROTECTION |
| T4.4.1 | Connectivity to Information Sharing Platforms |
| T4.4.2 | Information Released into Information Sharing Communities |
|  | INFORMATION SYSTEMS ACQUISITION, DEVELOPMENT |
| T7 | AND MAINTENANCE |
| T7.4 | CRYPTOGRAPHIC CONTROLS |
| T7.4.1 | Policy on the Use of Cryptographic Controls |
| T7.8 | SUPPLY CHAIN MANAGEMENT |
| T7.8.1 | Supply Chain Protection Strategy |
| T7.8.2 | Supplier Reviews |
|  | INFORMATION SECURITY INCIDENT MANAGEMENT |
| T8.1 | INFORMATION SECURITY INCIDENT MANAGEMENT POLICY |
| T8.1.1 | Information Security Incident Response Policy |
| T8.2 | MANAGEMENT OF INFORMATION SECURITY INCIDENTS |
| T8.2.2 | INCIDENT COMMENTS |
|  | Incident Classification |
| T8.3 | INFORMATION SECURITY EVENTS AND WEAKNESSES |
| T8.3.1 | REPORTING |
| T8.3.2 | Situational Awareness |
|  | Reporting Information Security Events |

--- Page 281 ---

# ANNEX F 

## TERMS AND DEFINITIONS

## TABLE 11: TERMS AND DEFINITIONS

| TERM | DEFINITION |
| :--: | :--: |
| ASSET | Anything that has value to the organization such as software, information, information systems. ${ }^{4}$ |
| AUDIT | An independent review of event logs and related activities performed to determine the adequacy of current security measures, to identify the degree of conformance with established policy or to develop recommendations for improvements to the security measures currently applied |
| AUTHENTICATION | Verifying the identity of a user, process, or device, often as a prerequisite to allowing access to resources in an information system. |
| AUTHENTICITY | The property of being genuine and being able to be verified and trusted; confidence in the validity of a transmission, a message, or message originator. See Authentication |
| AVAILABILITY | The property of being accessible and usable upon demand by an authorized entity ${ }^{4}$ |
| CERTIFICATION | A procedure by which a formal assurance statement is given that a deliverable conforms to a specified standard |
| CLOUD <br> COMPUTING | The practice of using a network of remote servers hosted on the Internet to store, manage, and process data, rather than a local server or a personal computer |
| CONFIDENTIALITY | The property that information is not made available or disclosed to unauthorized individuals, entities, or processes ${ }^{4}$ |
| CONTROL | Means of managing risk, including policies, procedures, guidelines, practices or organizational structures, which can be of administrative, technical, management, or legal nature ${ }^{4}$ <br> Note: Control is also used as a synonym for safeguard or countermeasure |
| CRITICAL ENTITY | An entity responsible for the investments in, and/or day-to-day operation of a particular critical information infrastructure |

--- Page 282 ---

| CRITICAL <br> INFORMATION <br> INFRASTRUCTURE | Physical and virtual information assets that support carrying-out of a critical function and the delivery of a critical service. |
| :--: | :--: |
| CRITICAL <br> INFORMATION <br> INFRASTRUCTURE <br> OPERATOR | An entity responsible for the investments in, and/or day-to-day operation of, a particular critical information infrastructure |
| CRITICAL <br> INFORMATION <br> INFRASTRUCTURE <br> PROTECTION | The protection of critical information infrastructure such as information assets, that support the delivery of a critical service |
| CRITICAL SECTOR | A sector identified at the national level that provides critical service(s). |
| CRITICAL SERVICE | Vital service, the disruption or destruction of which may have a debilitating impact on the national security, economy, society or any combination of these. |
| CRYPTOGRAPHIC SYSTEM | A related set of hardware or software used for cryptographic communication, processing or storage, and the administrative framework in which it operates |
| CYBERSECURITY | Cybersecurity is the set of technologies, processes, legislations, practices, and other required capabilities designed to protect the information infrastructure from disruption, breakdown, or misuse. |
| CYBERSPACE | Global electronic medium comprised of a network of interdependent information technology infrastructures, telecommunications networks and computer processing systems |
| DEMILITARIZED <br> ZONE (OR DMZ) | A small network with one or more servers that is kept separate from the core network, either on the outside of the firewall, or as a separate network protected by the firewall. Demilitarized zones usually provide public domain information to less trusted networks, such as the Internet |
| ENTITY CONTEXT | Refers to the set of entity information assets, practices, and standards that characterize core cyber security capabilities to establish a minimum level of information assurance within a given entity |

--- Page 283 ---

| FILTER | A hardware or software device that controls the flow of data in accordance with a security policy |
| :--: | :--: |
| FIREWALL | A network protection device that filters incoming and outgoing network data, based on a series of rules |
| TERM | DEFINITION |
| GATEWAY | Gateways connect two or more networks from different security domains to allow access to or transfer of information according to defined security policies. Some gateways can be automated through a combination of physical or software mechanisms |
| GUIDELINE | A description that clarifies what should be done and how, to achieve the objectives set out in policies ${ }^{4}$ |
| HACKTIVISTS | People that perform the act of hacking, or breaking into computer systems, for a politically or socially motivated purpose |
| HARDWARE | A generic term for any physical component of information and communication technology |
| HOST-BASED |  |
| INTRUSION <br> DETECTION SYSTEM <br> (HIDS OR IDS) | A security device, resident on a specific host, which monitors system activities for malicious or unwanted behavior |
| IATFS | Information Assurance Technical Forums are governance bodies that engage key stakeholders (such as industry leaders, experts, relevant entities, and sector regulators) in the development of the UAE IA Standards |
| IMPLEMENTING ENTITY | Refers to any entity implementing the UAE IA Standards - including critical entities mandated to implement these Standards, as well as any other entities implementing these Standards |
| INFORMATION <br> ASSET | A physical or virtual asset of ICT systems such as data, systems, facilities, network and computers |
| INFORMATION <br> ASSURANCE | Practice of protecting information and managing risks related to the use, processing, storage and transmission of information or data, and the systems and processes used for those purposes |
| INFORMATION SECURITY | Preservation of confidentiality, integrity and availability of information; in addition, other properties such as authenticity, accountability, nonrepudiation and reliability can also be involved ${ }^{4}$ |
| INFORMATION SECURITY EVENT | An identified occurrence of a system, service or network state indicating a possible breach of information security policy or failure of safeguards, or a previously unknown situation that may be security relevant ${ }^{4}$ |
| INFORMATION SECURITY INCIDENT | A single or a series of unwanted or unexpected information security events that have a significant probability of compromising business operations and threatening information security ${ }^{4}$ |

--- Page 284 ---

| INFORMATION SECURITY POLICY | A high-level document that describes how an entity protects its systems. The ISP is normally developed to cover all systems and can exist as a single document or as a set of related documents |
| :--: | :--: |
| TERM | DEFINITION |
| INFORMATION <br> SHARING <br> CAPABILITY | A set of policies, systems, and organizational roles needed to share information based on established requirements |
| INFORMATION <br> SHARING <br> COMMUNITY | Group of organizations that agree to share information |
| INTEGRITY | The property of safeguarding the accuracy and completeness of assets ${ }^{4}$ |
| KEY MANAGEMENT | The use and management of cryptographic keys and associated hardware and software. It includes their generation, registration, distribution, installation, usage, protection, storage, access, recovery and destruction |
| MALICIOUS CODE OR MALWARE | Any software that attempts to subvert the confidentiality, integrity or availability of a system. Types of malicious code include logic bombs, trapdoors, Trojans, viruses and worms |
| MANAGEMENT CONTROLS | The security controls (i.e., safeguards or countermeasures) for an information system that focus on the management of risk and the management of information systems security |
| MEDIA | A generic term for hardware that is used to store information |
| MEDIA DISPOSAL | The process of relinquishing control of media when no longer required, in a manner that ensures that no data can be recovered from the media |
| NATIONAL <br> CONTEXT | Refers to the set of national information assets, practices, and standards that characterize core cyber security capabilities to establish a minimum level of information assurance at a national level |
| NATIONAL CYBER RESPONSE FRAMEWORK | The program designed to increase situational awareness, rapidly identify and analyze incidents, and coordinate responses with national cyber security stakeholders |
| NETWORK DEVICE | Any device designed to facilitate the communication of information destined for multiple system users. For example: cryptographic devices, firewalls, routers, switches and hubs |
| NON-REPUDIATION | Protection against an individual falsely denying having performed a particular action. Provides the capability to determine whether a given individual took a particular action such as creating information, sending a message, approving information, and receiving a message. |
| POLICY | Overall intention and direction as formally expressed by management ${ }^{4}$ |

--- Page 285 ---

| TERM | DEFINITION |
| :--: | :--: |
| REGULATOR | A government body that sets regulations and monitors compliance and behavior of regulated entities in a particular sector (or market) |
| REMOTE ACCESS | Access to a system from a location not under the physical control of the system owner |
| REMOVABLE MEDIA | Storage media that can be easily removed from a system and is designed for removal |
| RESIDUAL RISK | The risk remaining after risk treatment ${ }^{4}$ |
| RISK | Combination of the probability of an event and its consequence ${ }^{4}$ |
| RISK ACCEPTANCE | Decision to accept a risk ${ }^{4}$ |
| RISK ANALYSIS | Systematic use of information to identify sources and to estimate the risk ${ }^{4}$ |
| RISK ASSESSMENT | Overall process of risk analysis and risk evaluation ${ }^{4}$ |
| RISK EVALUATION | Process of comparing the estimated risk against given risk criteria to determine the significance of the risk ${ }^{4}$ |
| RISK MANAGEMENT | Coordinated activities to direct and control an organization with regard to risk ${ }^{4}$ |
| RISK TREATMENT | Process of selection and implementation of measures to modify risk ${ }^{4}$ NOTE: In this International Standard the term 'control' is used as a synonym for 'measure' |
| SECTOR PLAN | Detailed plan developed by sector regulator and approved by NCSA outlining the actions, responsible entities and timelines necessary to address the highest levels of risk identified in the Sector/National Risk Assessments and guide implementation of related CII Cybersecurity and Protection Requirements. |
| SECTOR-SPECIFIC CIIP WORKING GROUP | Sector-specific governance body, chaired by NCSA and comprised of sector regulator, operators and other stakeholders to foster sector collaboration and support sector planning, implementation, and monitoring activities to elevate Critical Information Infrastructure Protection |
| SOFTWARE COMPONENT | An element of a system, including but not limited to, a database, operating system, network or web application |

[^0]
[^0]:    ${ }^{4}$ The definition is based on ISO/IEC Publications.

--- Page 286 ---

| TERM | DEFINITION |
| :--: | :--: |
| STATEMENT OF APPLICABILITY | Documented statement describing the control objectives and controls that are relevant and applicable to the organization's ISMS. |
|  | NOTE: Control objectives and controls are based on the results and conclusions of the risk assessment and risk treatment processes, legal or regulatory requirements, contractual obligations and the organization's business requirements for information security |
| SUPPLY CHAIN | The sequence of processes involved in the production and distribution of a product or a service |
| TECHNICAL CONTROLS | The security controls (i.e., safeguards or countermeasures) for an information system that are primarily implemented and executed by the information system through mechanisms contained in the hardware, software, or firmware components of the system |
| THIRD PARTY | That person or body that is recognized as being independent of the parties involved, as concerns the issue in question ${ }^{4}$ |
| THREAT | A potential cause of an unwanted incident, which may result in harm to a system or organization ${ }^{4}$ |
| THREAT AGENT | Any person or thing that acts - or has the power to act - to cause, carry, transmit, or support a threat |
| THREAT VECTOR | The method a threat uses to get to the target |
| TRUSTED <br> INFORMATION COMMUNICATION ENTITY | Autonomous organization supporting information exchange within an information sharing community |
| VULNERABILITY | A weakness of an asset or group of assets that can be exploited by one or more threats ${ }^{4}$ |
| WIRELESS COMMUNICATIONS | The transmission of data over a communications path using electromagnetic waves rather than a wired medium |

--- Page 287 ---

![img-16.jpeg](img-16.jpeg)
$\oplus$
![img-17.jpeg](img-17.jpeg)

--- Page 288 ---

# ANNEX G 

## BIBLIOGRAPHY

## TABLE 12: BIBLIOGRAPHY

## S.NO REPORTS AND STANDARDS

1 ISO/IEC 27001:2005 "Information technology - Security techniques - Information security management systems - Requirements"

2 ISO/IEC 27002:2005 "Information technology - Security techniques - Code of practice for Information security management"

3 ISO/IEC 27005:2005 "Information technology - Security techniques -Information security risk management"

4 ISO/IEC 27010:2012 "Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications"

5 ISO/IEC 27032:2012 "Information technology - Security techniques - Guidelines for cybersecurity"

6 SANS 20 Critical Security Controls for Effective Cyber Defense, Version 4.1

7 NIST 800-53 Revision 4 "Security and Privacy Controls for Federal Information Systems and Organizations"

8 Abu Dhabi Information Security Standards, Version 1 and Version 2

9 Verizon Data Breach Investigation Report, 2012

10 Symantec Internet Security Threat Report, April 2012

11 Kaspersky Global IT Security Risks, 2012

12 Microsoft Security Intelligence Report, June 2012

--- Page 289 ---

|  1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  3 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  4 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  5 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  6 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  7 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  8 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  9 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  10 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  11 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  12 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  13 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  14 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  15 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  16 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  17 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  18 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  19 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  20 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  21 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  22 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  23 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  24 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  25 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  26 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  27 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  28 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  29 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  30 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  31 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  32 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  33 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  34 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  35 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  36 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  37 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  38 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  39 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  40 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  41 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  42 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  43 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  44 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  45 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  46 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  47 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  48 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  49 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  50 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  51 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  52 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  53 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  54 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  55 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  56 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  57 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  58 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  59 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  60 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  61 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  62 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  63 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  64 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  65 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  66 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  67 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  68 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  69 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  70 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  71 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  72 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  73 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  74 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  75 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  76 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  77 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  78 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  79 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  80 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  81 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  82 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  83 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  84 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  85 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  86 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  87 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  88 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  89 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  90 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  91 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  92 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  93 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  94 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  95 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  96 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  97 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  98 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  99 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  100 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  101 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  102 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  103 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  104 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  105 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  106 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  107 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  108 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  109 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  110 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  111 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  112 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  113 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  114 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  115 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  116 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  117 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  118 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  119 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  120 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  121 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  122 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  123 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  124 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  125 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  126 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  127 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  128 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  129 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  130 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  131 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  132 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  133 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  134 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  135 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  136 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  137 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  138 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  139 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  140 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  141 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  142 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  143 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  144 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  145 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  146 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  147 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  148 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  149 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  150 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  151 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  152 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  153 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  154 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  155 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  156 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  157 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  158 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  159 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  160 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  161 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  162 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  163 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  164 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  165 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  166 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  167 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  168 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  169 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  170 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  171 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  172 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  173 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  174 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  175 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  176 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  177 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  178 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  179 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  180 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  181 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  182 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  183 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  184 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  185 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  186 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  187 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  188 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  189 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  190 | |  |  | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  191 | |  |  | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  |  | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  |  | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  |  | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 | |  |  | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 |  |  | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 |  |  | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 |  |  | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  191 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  1910 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  1911 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  192 |  |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  193 |  | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  194 |  | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  195 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  196 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 | |  | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  197 | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |   |
|  198 | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |   |
|  199 | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |   |
|  199 | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |   |
|  199 | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |   |
|  1910 | | | | | | | | | | |  |  |  |  |  |  |  |  |  |   |
|  1911 | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |   |
|  192 | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  193 | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  193 | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  193 | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  194 | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  194 | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  194 | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  195 | | | | | | | | | | | | |  |  |  |  |  |  |  |  |   |
|  195 | | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  195 | | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  196 | | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  196 | | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  197 | | | | | | | | | | | | |  |  |  |  |  |  |   |
|  197 | | | | | | | | | | | | |  |  |  |  |  |  |  |   |
|  197 | | | | | | | | | | | | |  |  |  |  |  |  |   |
|  198 | | | | | | | | | | | | |  |  |  |  |  |  |   |
|  198 | | | | | | | | | | | | |  |  |  |  |  |  |   |
|  199 | | | | | | | | | | | | |  |  |  |  |  |   |
|  199 | | | | | | | | | | | | | |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  | 

--- Page 290 ---

# (1) 

## HAPTER 07 APPENDIX

--- Page 291 ---

(1)
![img-18.jpeg](img-18.jpeg)

--- Page 292 ---

# APPENDIX 

Most of this information is derived from a variety of sources, including:

- ISO/IEC 27001:2005 "Information technology - Security techniques - Information security management systems - Requirements"
- ISO/IEC 27002:2005 "Information technology - Security techniques - Code of practice for Information security management"
- ISO/IEC 27005:2005 "Information technology - Security techniques - Information security risk management"
- ISO/IEC 27010:2012 "Information technology - Security techniques - Information security management for inter-sector and inter-organizational communications"
- ISO/IEC 27032:2012 "Information technology - Security techniques - Guidelines for cybersecurity"
- NIST Special Publication 800-53 Revision 4 "Security and Privacy Controls for Federal Information Systems and Organizations"
- Abu Dhabi Information Security Standards Version 1 and Version 2, developed by Abu Dhabi Systems and Information Centre (ADSIC)
- SANS 20 Critical Security Controls for Effective Cyber Defense Version 4.1

--- Page 293 ---

# 0 

![img-19.jpeg](img-19.jpeg)