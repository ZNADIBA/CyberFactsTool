import streamlit as st
import random

# List of facts with in-depth explanations
facts = [
    {
        "fact": "Phishing is a cyberattack technique used to trick users into revealing sensitive information.",
        "explanation": "Phishing is one of the most common and dangerous cyberattack methods. Cybercriminals impersonate trusted entities (like your bank or a popular website) to deceive you into giving them your personal details, such as login credentials or credit card numbers. Always be cautious when clicking on links or opening attachments in unsolicited emails!"
    },
    {
        "fact": "Malware is malicious software designed to harm computer systems.",
        "explanation": "Malware includes viruses, worms, and trojans, all created to damage your computer or steal your data. Once malware infects your device, it can corrupt files, slow down your system, or even give hackers unauthorized access to your information. Keep your system updated and install antivirus software to protect yourself!"
    },
    {
        "fact": "Ransomware is a type of malware that encrypts a victim's files and demands a ransom to decrypt them.",
        "explanation": "Ransomware is a nightmare for businesses and individuals alike. Once it infects a device, it locks or encrypts files, and the hacker demands payment (usually in cryptocurrency) to restore access. It's essential to have backups and avoid paying the ransom to discourage cybercriminals."
    },
    {
        "fact": "A firewall is a security system that monitors network traffic and blocks unauthorized access.",
        "explanation": "A firewall acts as a barrier between your internal network and the internet. It monitors incoming and outgoing traffic to prevent unauthorized access. Firewalls are critical in protecting your devices from cyberattacks, especially when connected to public or unsecured networks."
    },
    {
        "fact": "Encryption is the process of converting plain text into ciphertext to protect sensitive information.",
        "explanation": "Encryption turns readable data into unreadable code, ensuring that even if hackers intercept your information, they won't be able to decipher it. Encryption is vital for protecting sensitive data like passwords, financial transactions, and personal communications."
    },
    {
        "fact": "Cybercrime damages are projected to cost the world $10.5 trillion annually by 2025.",
        "explanation": "As the digital world expands, cybercrime becomes a more lucrative and widespread problem. This includes losses from data breaches, identity theft, fraud, and more. It's a wake-up call for individuals and organizations to prioritize cybersecurity."
    },
    {
        "fact": "A cyberattack occurs every 39 seconds.",
        "explanation": "That’s right — cyberattacks are happening constantly, and they often target individuals, companies, and governments. The increasing number of cyberattacks underscores the importance of staying vigilant and securing personal and business data."
    },
    {
        "fact": "The global cybersecurity workforce needs to grow by 65% to defend organizations effectively.",
        "explanation": "The demand for cybersecurity professionals is skyrocketing due to the growing number of cyber threats. There is a significant shortage of trained professionals, making it even more challenging for organizations to defend against cyberattacks."
    },
    {
        "fact": "More than 90% of successful cyberattacks start with phishing emails.",
        "explanation": "Phishing is the gateway for many attacks. It’s often the first step in stealing sensitive data, installing malware, or gaining unauthorized access. Knowing how to spot phishing emails can be the difference between staying secure and falling victim to a cyberattack."
    },
    {
        "fact": "Human error is responsible for 95% of cybersecurity breaches.",
        "explanation": "People are often the weakest link in cybersecurity. Whether it's clicking on a phishing link, using weak passwords, or misconfiguring a system, human mistakes are responsible for most breaches. Training employees and individuals in best practices is crucial to reducing these risks."
    },
    {
        "fact": "In 2023, ransomware attacks targeted businesses every 10 seconds.",
        "explanation": "The frequency of ransomware attacks in 2023 shows just how pervasive and destructive they’ve become. Every 10 seconds, a business is targeted, and these attacks often cripple organizations, causing significant downtime and financial loss."
    },
    {
        "fact": "The average cost of a data breach globally is $4.45 million.",
        "explanation": "Data breaches are costly, and the average global cost of one is a staggering $4.45 million. This includes legal fees, regulatory fines, lost business, and recovery costs. The financial impact is so severe that many companies fail to recover fully."
    },
    {
        "fact": "The healthcare industry has the highest average cost of a data breach, at $10.93 million.",
        "explanation": "The healthcare industry faces the highest average cost of a data breach because of the sensitive nature of health data. The breach of personal health information (PHI) involves significant regulatory fines, lawsuits, and a loss of patient trust."
    },
    {
        "fact": "Over 70% of organizations experienced at least one ransomware attack in 2022.",
        "explanation": "Ransomware attacks are becoming increasingly common, and in 2022, more than 70% of organizations experienced at least one. These attacks have become one of the most significant cybersecurity threats worldwide."
    },
    {
        "fact": "Phishing is the most common form of social engineering attack.",
        "explanation": "Phishing attacks are a primary form of social engineering, where attackers deceive individuals into disclosing sensitive information, such as login credentials or financial details. The technique often uses fake emails, texts, or websites to appear legitimate."
    },
    {
        "fact": "30% of phishing messages are opened by their recipients.",
        "explanation": "Phishing attacks are surprisingly effective, with 30% of phishing messages being opened. Once opened, they can lead to credential theft, malware infections, and unauthorized access to sensitive data."
    },
    {
        "fact": "Credential phishing accounted for 59% of phishing attacks in 2022.",
        "explanation": "Credential phishing is a major contributor to the rise of phishing attacks. In 2022, 59% of phishing attacks focused on stealing login credentials, which can then be used to gain unauthorized access to systems and data."
    },
    {
        "fact": "Business email compromise (BEC) scams cost organizations $43 billion between 2016 and 2022.",
        "explanation": "BEC scams, where cybercriminals impersonate executives or business partners to trick employees into transferring money or data, cost organizations an estimated $43 billion between 2016 and 2022. These scams often go undetected for long periods."
    },
    {
        "fact": "Deepfake technology is increasingly being used in phishing scams.",
        "explanation": "Deepfake technology, which creates realistic videos or audio clips of individuals, is increasingly being used in phishing attacks. Cybercriminals use deepfakes to impersonate trusted individuals, making their phishing attempts more convincing and harder to detect."
    },
    {
        "fact": "Spear phishing emails have a higher success rate due to personalization.",
        "explanation": "Spear phishing attacks are highly targeted, with emails often personalized to the victim. This increases the likelihood of the attack succeeding, as the attacker uses information about the individual or organization to make the message appear legitimate."
    },
    {
        "fact": "Fake LinkedIn profiles are a growing tool for social engineering.",
        "explanation": "Fake LinkedIn profiles are being used by cybercriminals to connect with and gather sensitive information from victims. By creating fake professional profiles, attackers can manipulate individuals into providing access to corporate networks or confidential data."
    },
    {
        "fact": "1 in 99 emails is a phishing attack.",
        "explanation": "Statistically, 1 out of every 99 emails you receive is a phishing attempt. With phishing becoming more widespread, it’s important to stay vigilant and verify the authenticity of emails before clicking links or downloading attachments."
    },
    {
        "fact": "50% of phishing sites now use HTTPS to appear more legitimate.",
        "explanation": "Phishing websites are becoming more sophisticated, and half of them now use HTTPS to appear secure. This tactic is designed to trick users into thinking the site is legitimate when it’s actually designed to steal personal information."
    },
    {
        "fact": "Phishing emails often impersonate banks, payment systems, or major tech companies.",
        "explanation": "Phishing emails frequently impersonate trusted organizations, such as banks or popular tech companies. By using familiar branding and logos, attackers aim to deceive recipients into clicking on malicious links or downloading infected attachments."
    },
    {
        "fact": "Multi-factor authentication can reduce phishing risks significantly.",
        "explanation": "Multi-factor authentication (MFA) adds an extra layer of security by requiring users to provide two or more forms of verification before accessing an account. This significantly reduces the risk of falling victim to phishing attacks, as stolen credentials alone aren’t enough to gain access."
    },
    {
        "fact": "68.5% of organizations hit by ransomware in 2022 paid the ransom.",
        "explanation": "Despite the risks, 68.5% of organizations that were hit by ransomware in 2022 paid the ransom to regain access to their encrypted data. However, paying the ransom doesn’t guarantee recovery and only encourages cybercriminals to continue their attacks."
    },
    {
        "fact": "The average ransom payment in 2023 was $258,000.",
        "explanation": "Ransomware attacks have become a lucrative business for cybercriminals, with the average ransom payment in 2023 reaching $258,000. The growing frequency of these attacks highlights the need for robust security measures to prevent such incidents."
    },
    {
        "fact": "Only 65% of companies that pay a ransom recover all their data.",
        "explanation": "Even when companies pay the ransom, there’s no guarantee they will recover all of their data. In fact, only 65% of companies that pay a ransom manage to fully restore their files, making backups and prevention critical."
    },
    {
        "fact": "Ransomware-as-a-Service (RaaS) is a growing trend in the cybercrime ecosystem.",
        "explanation": "Ransomware-as-a-Service (RaaS) allows less experienced cybercriminals to launch ransomware attacks by renting malware from more sophisticated hackers. This business model has made ransomware attacks more widespread and accessible."
    },
    {
        "fact": "Cybercriminals often use double extortion tactics: encrypting data and threatening to leak it.",
        "explanation": "Double extortion tactics involve not only encrypting the victim's data but also threatening to leak it publicly unless the ransom is paid. This added pressure makes it harder for organizations to resist paying, as the threat of a data leak can have severe reputational and financial consequences."
    },
    {
        "fact": "The Conti ransomware group reportedly earned $180 million in 2021 alone.",
        "explanation": "The Conti ransomware group is one of the most notorious cybercrime organizations, and it reportedly earned $180 million in 2021 through ransom payments. The group targets high-value organizations, encrypting critical data and demanding large ransoms."
    },
    {
        "fact": "Small and medium-sized businesses are increasingly targeted by ransomware attacks.",
        "explanation": "While large corporations have been prime targets for ransomware, small and medium-sized businesses (SMBs) are increasingly being targeted. SMBs often lack the resources and defenses needed to withstand cyberattacks, making them an attractive target for cybercriminals."
    },
    {
        "fact": "A ransomware attack happens every 14 seconds globally.",
        "explanation": "Ransomware attacks are happening at an alarming rate, with one occurring every 14 seconds worldwide. This highlights the urgency for organizations and individuals to adopt robust cybersecurity practices to defend against these frequent and damaging attacks."
    },
    {
        "fact": "In 2021, Colonial Pipeline paid $4.4 million in Bitcoin after a ransomware attack.",
        "explanation": "In 2021, Colonial Pipeline, one of the largest fuel pipelines in the U.S., was hit by a ransomware attack. The company paid $4.4 million in Bitcoin to the attackers to regain control of its systems, though much of the ransom was later recovered by the FBI."
    },
    {
        "fact": "Backups can prevent ransom payments but are often targeted by attackers.",
        "explanation": "Having secure backups is one of the best defenses against ransomware attacks, as it allows organizations to restore their data without paying the ransom. However, attackers are increasingly targeting backups, making it crucial to keep backups secure and offline."
    },
    {
        "fact": "In 2022, over 22 billion records were exposed due to data breaches.",
        "explanation": "In 2022, data breaches exposed over 22 billion records, affecting millions of individuals and organizations. The sheer volume of exposed data underscores the need for robust data protection measures and response strategies."
    },
    {
        "fact": "The average time to identify a data breach is 277 days.",
        "explanation": "On average, it takes organizations 277 days to detect a data breach. During this time, attackers can access sensitive data and cause significant damage. Quick detection is key to minimizing the impact of a breach."
    },
    {
        "fact": "Insider threats cause about 20% of all data breaches.",
        "explanation": "While external threats are commonly discussed, insider threats—whether intentional or accidental—are responsible for about 20% of all data breaches. Employees with access to sensitive data can pose a significant risk to an organization."
    },
    {
        "fact": "Misconfigured cloud settings account for 15% of data breaches.",
        "explanation": "Misconfigurations in cloud settings are a leading cause of data breaches, responsible for 15% of incidents. This occurs when organizations fail to properly secure their cloud environments, leaving data exposed to unauthorized access."
    },
    {
        "fact": "Facebook experienced one of the largest breaches, exposing 533 million users' data in 2021.",
        "explanation": "In 2021, Facebook suffered one of the largest data breaches, exposing personal information of 533 million users. The breach involved data like phone numbers and user IDs, which were later found circulating on the dark web."
    },
    {
        "fact": "Marriott's data breaches between 2014 and 2018 exposed 500 million guest records.",
        "explanation": "Marriott's data breaches between 2014 and 2018 compromised over 500 million guest records. This breach included sensitive information such as passport numbers and credit card details, significantly damaging Marriott's reputation and security posture."
    },
    {
        "fact": "Equifax's 2017 breach affected 147 million Americans.",
        "explanation": "In 2017, Equifax, one of the largest credit reporting agencies, experienced a massive data breach that affected 147 million Americans. The breach exposed sensitive financial and personal data, including social security numbers, making the victims vulnerable to identity theft."
    },
    {
        "fact": "Data breaches often result in lawsuits and regulatory fines.",
        "explanation": "When a data breach occurs, affected organizations often face lawsuits from customers, partners, and other stakeholders. Additionally, regulatory bodies may impose fines for failing to adequately protect user data, further exacerbating the financial impact."
    },
    {
        "fact": "Cybercriminals frequently target personal identifiable information (PII) for resale on the dark web.",
        "explanation": "Personal Identifiable Information (PII) is highly sought after by cybercriminals because it can be sold on the dark web. PII, such as social security numbers and credit card details, is valuable for identity theft and fraud."
    },
    {
        "fact": "Encryption and tokenization are vital in protecting sensitive data.",
        "explanation": "Encryption and tokenization are key techniques used to protect sensitive data. Encryption transforms data into unreadable code, while tokenization replaces sensitive data with unique identifiers, both helping to prevent unauthorized access."
    },
    {
        "fact": "99% of cloud security failures are due to user misconfigurations.",
        "explanation": "The vast majority of cloud security incidents (99%) are caused by user misconfigurations. This highlights the importance of proper training and oversight to prevent errors that could expose cloud data and services to vulnerabilities."
    },
    {
        "fact": "Multi-cloud environments are more prone to breaches than single-cloud setups.",
        "explanation": "Multi-cloud environments, where organizations use multiple cloud providers, can increase security risks. The complexity of managing multiple platforms often leads to misconfigurations and gaps in security, making these environments more vulnerable to breaches than single-cloud setups."
    },
    {
        "fact": "Cybercriminals increasingly target API vulnerabilities in cloud services.",
        "explanation": "APIs (Application Programming Interfaces) are often targeted by cybercriminals because they can provide access to sensitive data and services. Many cloud applications expose APIs, and if they’re not properly secured, they become prime targets for exploitation."
    },
    {
        "fact": "Lack of visibility is the biggest challenge in cloud security.",
        "explanation": "A significant challenge in securing cloud environments is the lack of visibility. Organizations may struggle to monitor and track activities across their cloud services, leaving gaps in security that cybercriminals can exploit."
    },
    {
        "fact": "Over 90% of enterprises have experienced a cloud security incident.",
        "explanation": "Cloud security incidents are widespread, with over 90% of enterprises having encountered at least one. These incidents can range from data leaks to unauthorized access, underscoring the need for robust security practices in the cloud."
    },
    {
        "fact": "Stolen cloud credentials are a significant cause of cloud data breaches.",
        "explanation": "Stolen cloud credentials are a major factor in cloud data breaches. Cybercriminals who gain access to an organization’s cloud login information can steal sensitive data or compromise cloud services, leading to significant security incidents."
    },
    {
        "fact": "DevOps environments often introduce misconfigurations leading to vulnerabilities.",
        "explanation": "DevOps environments, which combine development and operations teams to speed up software deployment, can sometimes introduce security misconfigurations. These misconfigurations, if not addressed, can lead to vulnerabilities and increase the risk of a breach."
    },
    {
        "fact": "Cloud-native security solutions are becoming more critical for enterprises.",
        "explanation": "As organizations continue to adopt cloud services, cloud-native security solutions are becoming essential. These solutions are specifically designed to protect cloud environments and provide better protection against the unique security challenges posed by the cloud."
    },
    {
        "fact": "The use of public Wi-Fi can expose cloud credentials.",
        "explanation": "Public Wi-Fi networks are notoriously insecure, and using them can expose cloud credentials to cybercriminals. Attackers can intercept data sent over unsecured networks, including login details for cloud accounts, putting sensitive data at risk."
    },
    {
        "fact": "Zero-trust architecture is essential for secure cloud deployments.",
        "explanation": "Zero-trust architecture assumes that no user or device, whether inside or outside the network, can be trusted by default. This approach ensures that every access request is thoroughly authenticated, making it a vital strategy for securing cloud deployments."
    },
    {
        "fact": "Mobile malware increased by 54% in 2022.",
        "explanation": "Mobile malware saw a sharp increase of 54% in 2022, with attackers targeting smartphones and mobile devices. These devices, often used for banking and communication, provide a rich source of personal data that cybercriminals can exploit."
    },
    {
        "fact": "Android devices are targeted more frequently than iOS devices.",
        "explanation": "Android devices are targeted more frequently by malware than iOS devices. This is primarily due to Android’s more open ecosystem and its larger user base, making it a more attractive target for attackers."
    },
    {
        "fact": "IoT devices are expected to exceed 75 billion by 2025, increasing attack surfaces.",
        "explanation": "The rapid growth of the Internet of Things (IoT) is expected to result in over 75 billion connected devices by 2025. This growth significantly increases the potential attack surface, as each device can be exploited by cybercriminals if not properly secured."
    },
    {
        "fact": "98% of IoT device traffic is unencrypted.",
        "explanation": "A staggering 98% of IoT device traffic is unencrypted, leaving these devices vulnerable to interception and exploitation. Without proper encryption, the sensitive data transmitted by IoT devices is at risk of being compromised."
    },
    {
        "fact": "Smart home devices are common targets for hackers.",
        "explanation": "Smart home devices, such as thermostats, cameras, and voice assistants, are increasingly targeted by hackers. These devices often have weak security, making them an attractive entry point for cybercriminals to infiltrate home networks."
    },
    {
        "fact": "Mobile banking malware is on the rise globally.",
        "explanation": "Mobile banking malware has been on the rise globally, with attackers using it to steal money and financial data from victims. These malicious apps can capture login credentials, perform fraudulent transactions, or even intercept two-factor authentication codes."
    },
    {
        "fact": "Default passwords on IoT devices pose significant risks.",
        "explanation": "Many IoT devices come with default passwords that are rarely changed by users. These weak passwords are easy targets for cybercriminals, who can gain unauthorized access and use the devices for malicious purposes."
    },
    {
        "fact": "SIM swapping attacks have become a popular form of identity theft.",
        "explanation": "SIM swapping attacks have surged in popularity, where attackers convince a mobile carrier to transfer a victim’s phone number to a new SIM card. This gives attackers access to the victim’s calls, messages, and potentially sensitive accounts like bank accounts or social media."
    },
    {
        "fact": "Mobile ransomware attacks are becoming more sophisticated.",
        "explanation": "Mobile ransomware attacks are becoming more sophisticated, with attackers using tactics such as encryption of files and apps on mobile devices, demanding ransom payments for decryption keys, and threatening to release sensitive data."
    },
    {
        "fact": "Wearable devices can expose sensitive data to attackers.",
        "explanation": "Wearable devices, such as fitness trackers and smartwatches, can expose sensitive data like health information and location data. If not properly secured, these devices can be exploited by attackers to gain access to personal details."
    },
    {
        "fact": "The average person reuses a password across 5 different sites.",
        "explanation": "A major security risk is password reuse. On average, people use the same password across five different websites, making it easier for attackers to gain access to multiple accounts once a password is compromised."
    },
    {
        "fact": "23 million people still use '123456' as a password.",
        "explanation": "Despite the well-known risks of weak passwords, 23 million people still use '123456' as their password. This simple and common password makes it incredibly easy for attackers to break into accounts."
    },
    {
        "fact": "Passwordless authentication methods are gaining traction.",
        "explanation": "Passwordless authentication methods, such as biometrics, push notifications, and hardware tokens, are gaining popularity due to their ability to enhance security while offering a more convenient user experience by eliminating the need for traditional passwords."
    },
    {
        "fact": "Multi-factor authentication can block up to 99.9% of automated attacks.",
        "explanation": "Multi-factor authentication (MFA) significantly strengthens security by requiring more than just a password. It can block up to 99.9% of automated attacks, such as credential stuffing, by adding an additional layer of verification."
    },
    {
        "fact": "Weak passwords account for 81% of data breaches.",
        "explanation": "Weak or easily guessed passwords are responsible for the majority of data breaches. Attackers exploit weak passwords through methods like brute force or dictionary attacks to gain unauthorized access to systems and data."
    },
    {
        "fact": "Biometric authentication systems are more secure but not foolproof.",
        "explanation": "Biometric authentication, such as fingerprint or facial recognition, is considered more secure than traditional passwords. However, it is not foolproof and can be bypassed using advanced techniques like spoofing or deepfakes."
    },
    {
        "fact": "Dictionary attacks rely on common password combinations.",
        "explanation": "Dictionary attacks use a list of common passwords or word combinations to systematically attempt to break into accounts. These attacks are effective against users who choose simple or common passwords."
    },
    {
        "fact": "Credential stuffing attacks exploit reused passwords across platforms.",
        "explanation": "Credential stuffing attacks take advantage of users who reuse passwords across multiple sites. Cybercriminals steal login credentials from one breach and try them across various platforms, increasing the likelihood of success."
    },
    {
        "fact": "Password managers help users maintain strong, unique passwords.",
        "explanation": "Password managers securely store and manage passwords, enabling users to generate and maintain strong, unique passwords for every account without needing to remember them. This greatly reduces the risks associated with weak or reused passwords."
    },
    {
        "fact": "Complex passwords should contain at least 12 characters, including symbols and numbers.",
        "explanation": "For strong security, passwords should be at least 12 characters long and include a combination of uppercase letters, lowercase letters, numbers, and symbols. This complexity makes it much harder for attackers to crack the password."
    },
    {
        "fact": "AI is increasingly used in both cyber defense and attacks.",
        "explanation": "AI is being leveraged in cybersecurity for defense purposes, such as detecting threats and automating responses, but it is also being used by cybercriminals to automate attacks and adapt their strategies in real time."
    },
    {
        "fact": "Machine learning algorithms can detect anomalies in network traffic.",
        "explanation": "Machine learning algorithms can analyze network traffic patterns and detect anomalies that may indicate a potential security breach or unauthorized activity, helping to detect and mitigate threats before they cause harm."
    },
    {
        "fact": "Endpoint detection and response (EDR) tools provide proactive threat mitigation.",
        "explanation": "EDR tools are designed to monitor endpoints, such as computers and mobile devices, for signs of malicious activity. They provide real-time threat detection, prevention, and response, helping organizations mitigate risks proactively."
    },
    {
        "fact": "Encryption is the backbone of secure communication protocols.",
        "explanation": "Encryption is essential for protecting sensitive data during transmission over networks. It ensures that even if data is intercepted, it cannot be read without the correct decryption key."
    },
    {
        "fact": "Firewalls remain a foundational cybersecurity technology.",
        "explanation": "Firewalls are a fundamental component of network security, acting as a barrier between trusted and untrusted networks. They help prevent unauthorized access to internal systems and mitigate external threats."
    },
    {
        "fact": "VPNs can protect users from unsecured networks but are not foolproof.",
        "explanation": "Virtual Private Networks (VPNs) protect users by encrypting their internet traffic, especially on unsecured networks like public Wi-Fi. However, they are not immune to attacks, and vulnerabilities in VPNs can still be exploited by cybercriminals."
    },
    {
        "fact": "Zero Trust Network Access (ZTNA) is replacing traditional VPNs in enterprises.",
        "explanation": "Zero Trust Network Access (ZTNA) is becoming a preferred solution over traditional VPNs because it operates on the principle of 'never trust, always verify,' ensuring that every user and device is thoroughly authenticated before accessing company resources."
    },
    {
        "fact": "Intrusion detection systems (IDS) monitor for suspicious activities.",
        "explanation": "Intrusion Detection Systems (IDS) are used to monitor network traffic for signs of suspicious activity or potential security breaches. When an intrusion attempt is detected, IDS alerts administrators to take action."
    },
    {
        "fact": "SIEM platforms centralize threat intelligence and response.",
        "explanation": "Security Information and Event Management (SIEM) platforms centralize logs and data from across an organization's systems to provide real-time threat intelligence, allowing faster detection, analysis, and response to security incidents."
    },
    {
        "fact": "Behavioral analytics can identify insider threats.",
        "explanation": "Behavioral analytics uses machine learning to analyze patterns in user behavior. It helps identify insider threats by detecting deviations from normal activities, such as unauthorized access to sensitive data or systems."
    },
    {
        "fact": "Cybercrime is the fastest-growing form of crime globally.",
        "explanation": "Cybercrime is increasing rapidly worldwide as more people, businesses, and services become digitized. This type of crime spans from identity theft to sophisticated hacking operations, making it a significant threat to global security."
    },
    {
        "fact": "The dark web hosts marketplaces for stolen data, ransomware kits, and hacking tools.",
        "explanation": "The dark web is a hub for illegal activities, including the buying and selling of stolen personal data, ransomware kits, and hacking tools. Cybercriminals use this space to anonymously exchange information and resources for malicious activities."
    },
    {
        "fact": "Cybercriminals increasingly use cryptocurrencies for transactions.",
        "explanation": "Cryptocurrencies, due to their anonymity and ease of transfer, are increasingly being used by cybercriminals to facilitate transactions, including paying for ransomware, buying stolen data, or moving illicit funds."
    },
    {
        "fact": "Advanced Persistent Threats (APTs) often target critical infrastructure.",
        "explanation": "Advanced Persistent Threats (APTs) are highly sophisticated cyberattacks typically aimed at critical infrastructure such as energy, utilities, and telecommunications. These attacks are usually state-sponsored and involve long-term, stealthy efforts to compromise systems."
    },
    {
        "fact": "Hacktivism is on the rise as geopolitical tensions grow.",
        "explanation": "Hacktivism, where cyberattacks are launched for political or social causes, is growing as geopolitical tensions rise. Hacktivists may target government systems, corporations, or organizations they believe are responsible for social or political injustices."
    },
    {
        "fact": "Cryptojacking attacks hijack computing power to mine cryptocurrency.",
        "explanation": "Cryptojacking is a type of cyberattack where attackers hijack a victim’s computing power to mine cryptocurrency without their knowledge. This can slow down systems and lead to increased energy consumption."
    },
    {
        "fact": "State-sponsored cyberattacks are becoming more sophisticated.",
        "explanation": "State-sponsored cyberattacks have become more sophisticated in recent years, often targeting other nations' critical infrastructure, intellectual property, or private sector organizations for espionage, sabotage, or economic advantage."
    },
    {
        "fact": "Financially motivated attacks are the most common motive for cybercriminals.",
        "explanation": "Financial gain is the primary motivation behind most cyberattacks. Cybercriminals are increasingly targeting individuals, companies, and governments to steal sensitive information, extort money, or commit fraud."
    },
    {
        "fact": "Malware-as-a-Service (MaaS) enables low-skill attackers to launch sophisticated attacks.",
        "explanation": "Malware-as-a-Service (MaaS) provides attackers with ready-made, customizable malicious software that requires little technical skill to use. This has lowered the barrier to entry for cybercriminals, enabling even low-skill attackers to launch complex cyberattacks."
    },
    {
        "fact": "Cyberattacks on supply chains increased by 51% in 2022.",
        "explanation": "Cyberattacks targeting supply chains have surged by 51% in 2022, as cybercriminals exploit vulnerabilities in third-party vendors and partners to gain access to larger organizations. These attacks can disrupt production and cause significant financial damage."
  
  },
    {
        "fact": "40% of industrial control systems experienced cyber incidents in 2022.",
        "explanation": "In 2022, 40% of industrial control systems (ICS) were targeted by cyber incidents. These systems, which control essential infrastructure like water treatment, electricity, and manufacturing processes, are increasingly being targeted due to their critical nature."
    },
    {"fact": "Publicly disclosing a data breach can impact stock prices by 7.5% on average.",
     "explanation": "Publicly disclosing a data breach can cause a significant drop in stock prices, with companies experiencing an average decline of 7.5%. This is due to the loss of consumer trust and the potential legal and financial consequences that follow a breach."},
    
    {"fact": "Recovery costs are often double the ransom amount.",
     "explanation": "After a ransomware attack, the costs for recovery can exceed the ransom paid to the attackers. This includes expenses for system restoration, lost productivity, and legal or compliance-related costs."},
    
    {"fact": "Forensic analysis is critical for understanding attack vectors.",
     "explanation": "Forensic analysis helps organizations determine how an attack occurred, which vulnerabilities were exploited, and the extent of the damage. It is essential for improving future defenses and recovering from the breach."},
    
    {"fact": "Notifying customers after a breach is legally required in most jurisdictions.",
     "explanation": "In many regions, businesses are legally obligated to notify affected customers about a data breach. This transparency helps protect individuals' rights and ensures compliance with data protection laws."},
    
    {"fact": "A good backup strategy should follow the 3-2-1 rule: 3 copies, 2 media types, 1 offsite.",
     "explanation": "The 3-2-1 backup rule recommends keeping three copies of data, using two different types of storage media, and storing one copy offsite. This ensures that data is protected and recoverable in case of a cyberattack or disaster."},
    
    {"fact": "Malware attacks increased by 358% in 2022.",
     "explanation": "Malware attacks saw a dramatic increase of 358% in 2022. Cybercriminals are continuously evolving their tactics, leading to higher frequencies of attacks and more complex threats targeting individuals and organizations."},
    
    {"fact": "Trojan horses account for 51% of all malware infections.",
     "explanation": "Trojan horses make up over half of all malware infections. These malicious programs disguise themselves as legitimate software to trick users into installing them, often giving attackers unauthorized access to systems."},
    
    {"fact": "Keyloggers are often used to steal sensitive login credentials.",
     "explanation": "Keyloggers record keystrokes on a device, allowing attackers to capture sensitive information like login credentials and credit card details. These are often used in financial and identity theft scams."},
    
    {"fact": "Adware, while less harmful, is still a cybersecurity threat.",
     "explanation": "Adware can disrupt system performance and steal personal information, even though it is often less malicious than other types of malware. It typically bombards users with unwanted ads, but it can lead to privacy issues."},
    
    {"fact": "Rootkits hide in operating system kernels, making them difficult to detect.",
     "explanation": "Rootkits are a type of malware that hide deep within the operating system, often in the kernel, making them difficult to detect. They allow attackers to maintain access to a system while avoiding detection."},
    
    {"fact": "Botnets like Emotet have been used in massive spam campaigns.",
     "explanation": "Botnets such as Emotet are networks of infected devices used to send out large volumes of spam emails, often spreading malware and ransomware. These campaigns can cause significant damage to businesses and individuals alike."},
    
    {"fact": "Spyware often targets mobile devices to steal user data.",
     "explanation": "Spyware targets mobile devices to steal sensitive data, including location, messages, and browsing history. This information can be exploited for identity theft or sold on the dark web."},
    
    {"fact": "Polymorphic malware changes its code to evade detection.",
     "explanation": "Polymorphic malware constantly changes its code to avoid detection by traditional antivirus programs. This makes it challenging for security systems to detect and remove the malware."},
    
    {"fact": "The WannaCry ransomware attack affected over 200,000 systems in 2017.",
     "explanation": "The WannaCry ransomware attack in 2017 affected more than 200,000 systems across 150 countries, exploiting a vulnerability in Microsoft Windows. It caused widespread disruption, especially in healthcare systems."},
    
    {"fact": "Malware campaigns increasingly target macOS users.",
     "explanation": "Malware campaigns have shifted focus towards macOS users, who were once considered less likely to be targeted. As macOS usage grows, so does the interest of cybercriminals in exploiting vulnerabilities in Apple's operating system."},
    
    {"fact": "White hat hackers help companies find vulnerabilities in their systems.",
     "explanation": "White hat hackers, also known as ethical hackers, are hired by organizations to identify and fix security vulnerabilities before malicious hackers can exploit them. Their work is essential in strengthening cybersecurity defenses."},
    
    {"fact": "Bug bounty programs paid over $200 million in rewards by 2023.",
     "explanation": "Bug bounty programs have become a key strategy in cybersecurity, with over $200 million paid in rewards by 2023. These programs incentivize ethical hackers to find vulnerabilities and report them to the companies responsible."},
    
    {"fact": "Ethical hackers use tools like Metasploit and Burp Suite.",
     "explanation": "Ethical hackers use specialized tools like Metasploit for testing system vulnerabilities and Burp Suite for web application security testing. These tools are integral to finding and fixing weaknesses in systems before they can be exploited."},
    
    {"fact": "Penetration testing helps organizations identify weaknesses before attackers do.",
     "explanation": "Penetration testing involves simulating cyberattacks to identify vulnerabilities in an organization's defenses. By conducting these tests, businesses can proactively strengthen their security and prevent real attacks."},
    
    {"fact": "The Certified Ethical Hacker (CEH) certification is a common credential for white hats.",
     "explanation": "The CEH certification is widely recognized in the cybersecurity industry as proof of a hacker's skills in identifying and fixing security vulnerabilities. It is a key credential for ethical hackers."},
    
    {"fact": "Red teams simulate attackers, while blue teams focus on defense.",
     "explanation": "Red teams simulate cyberattacks to test an organization's defenses, while blue teams focus on preventing and responding to these attacks. Together, they ensure comprehensive cybersecurity protection."},
    
    {"fact": "Purple teams combine offensive and defensive strategies for better security.",
     "explanation": "Purple teams blend the efforts of red and blue teams, allowing for a more cohesive approach to cybersecurity. This combination of offensive and defensive strategies improves overall security posture."},
    
    {"fact": "Social engineering is often tested during penetration assessments.",
     "explanation": "Social engineering techniques, such as phishing or pretexting, are often tested during penetration assessments to evaluate how well employees respond to deceptive tactics and prevent information breaches."},
    
    {"fact": "Hackathons sometimes include ethical hacking challenges.",
     "explanation": "Hackathons often feature ethical hacking challenges, where participants are tasked with finding vulnerabilities or fixing security issues within a limited time. These events encourage innovation in cybersecurity solutions."},
    
    {"fact": "Ethical hackers are often employed by large organizations to bolster security.",
     "explanation": "Large organizations hire ethical hackers to conduct regular security audits, penetration tests, and vulnerability assessments. Their goal is to proactively address security flaws and protect against potential attacks."},
    
    {"fact": "AI-powered cybersecurity tools can reduce response times by up to 96%.",
     "explanation": "AI-powered tools in cybersecurity can significantly improve response times to incidents. By automating threat detection and analysis, AI helps reduce the time it takes to mitigate potential attacks by up to 96%."},
    
    {"fact": "AI can predict threats based on historical attack patterns.",
     "explanation": "AI algorithms can analyze historical attack patterns and predict future threats. By recognizing trends and anomalies in data, AI can help organizations prepare for and prevent potential cyberattacks."},
    
    {"fact": "Machine learning algorithms help detect zero-day vulnerabilities.",
     "explanation": "Machine learning algorithms are increasingly used to detect zero-day vulnerabilities, which are previously unknown flaws that attackers can exploit before a fix is available. These algorithms help identify risks faster and more accurately."},
    
    {"fact": "Adversarial machine learning is used to exploit weaknesses in AI systems.",
     "explanation": "Adversarial machine learning involves manipulating AI systems by feeding them data specifically designed to confuse or mislead them. This can be used to bypass security measures or compromise AI-driven applications."},
    
    {"fact": "AI is being used to automate phishing campaigns.",
     "explanation": "Cybercriminals are using AI to automate and improve phishing campaigns, making them more targeted and convincing. AI can craft personalized phishing emails that are harder to detect by traditional security systems."},
    
    {"fact": "Natural language processing helps detect phishing emails.",
     "explanation": "Natural language processing (NLP) techniques are used to analyze the content of emails and identify signs of phishing. By examining writing patterns, NLP can flag suspicious messages and protect users from scams."},
    
    {"fact": "AI tools are being integrated into security operations centers (SOCs).",
     "explanation": "AI-powered tools are being integrated into security operations centers (SOCs) to enhance threat detection, incident response, and overall security monitoring. AI helps automate tasks and allows SOC analysts to focus on high-priority threats."},
    
    {"fact": "Attackers increasingly use AI to bypass CAPTCHA systems.",
     "explanation": "CAPTCHA systems, which are designed to differentiate between human and automated users, are increasingly being bypassed using AI. Attackers use machine learning models to solve CAPTCHAs and gain unauthorized access to websites."},
    
    {"fact": "Behavioral AI can identify anomalous activities on user accounts.",
     "explanation": "Behavioral AI can detect anomalous activities on user accounts by analyzing patterns in behavior. It can identify suspicious login attempts, unusual transactions, or other behaviors that may indicate a security breach."},
    
    {"fact": "ChatGPT-like models can assist both defenders and attackers in crafting scripts.",
     "explanation": "AI models like ChatGPT can be used by both defenders and attackers to automate script generation for cybersecurity tasks. These tools can streamline tasks such as vulnerability assessments, penetration testing, and even malicious activities."},
    
    {"fact": "Blockchain offers inherent security but is not immune to attacks.",
     "explanation": "Blockchain technology offers inherent security features such as decentralized verification, but it is not immune to attacks. Hackers can exploit vulnerabilities in smart contracts or cryptocurrency exchanges."},
    
    {"fact": "$4 billion in cryptocurrency was stolen through hacks in 2022.",
     "explanation": "In 2022, cybercriminals stole $4 billion worth of cryptocurrency through various hacks and exploits. The growing popularity of digital currencies has made them a major target for cyberattacks."},
    
    {"fact": "Decentralized exchanges (DEXs) are common targets for cybercriminals.",
     "explanation": "Decentralized exchanges (DEXs), which allow users to trade cryptocurrency directly with each other, are increasingly targeted by cybercriminals due to their lack of centralized security controls."},
    
    {"fact": "Smart contracts can contain exploitable vulnerabilities.",
     "explanation": "Smart contracts, which are self-executing contracts with the terms directly written into code, can have vulnerabilities that attackers can exploit. Flaws in the code can lead to financial losses or unauthorized access."},
    
    {"fact": "Cryptojacking attacks surged by 30% in 2023.",
     "explanation": "Cryptojacking attacks, where attackers hijack a victim’s computing power to mine cryptocurrency, surged by 30% in 2023. These attacks often go unnoticed while draining system resources."},
    
    {"fact": "Bitcoin wallets are frequently targeted for phishing scams.",
     "explanation": "Phishing scams targeting Bitcoin wallets have become more common, as attackers attempt to steal private keys or login credentials from cryptocurrency users through deceptive emails or websites."},
    
    {"fact": "Public keys must be secured to prevent identity theft.",
     "explanation": "Public keys, which are part of the encryption process in cryptocurrency transactions, must be kept secure to prevent identity theft and unauthorized transactions."},
    
    {"fact": "The Mt. Gox hack of 2014 remains one of the largest cryptocurrency thefts.",
     "explanation": "The Mt. Gox hack of 2014 remains one of the largest cryptocurrency thefts in history, where attackers stole approximately 850,000 Bitcoins from the exchange. The hack had a lasting impact on the cryptocurrency market."},
    
    {"fact": "Blockchain technology is being explored for secure identity management.",
     "explanation": "Blockchain is being explored for secure identity management due to its decentralized nature and ability to provide tamper-proof records. It could potentially replace traditional identity management systems."},
    
    {"fact": "2FA is essential for securing cryptocurrency accounts.",
     "explanation": "Two-factor authentication (2FA) is critical for securing cryptocurrency accounts. It adds an extra layer of protection by requiring users to provide two forms of identification before accessing their accounts."},
    
    {"fact": "Cyber warfare is considered the fifth domain of warfare.",
     "explanation": "Cyber warfare is now recognized as the fifth domain of warfare, alongside land, sea, air, and space. Nation-states use cyberattacks to disrupt critical infrastructure and achieve strategic objectives."},
    
    {"fact": "Stuxnet was one of the first-known cyber weapons targeting infrastructure.",
     "explanation": "Stuxnet was a highly sophisticated cyber weapon that targeted industrial control systems, specifically the Iranian nuclear program. It is considered one of the first known acts of cyber warfare."},
    
    {"fact": "Nation-state actors are behind many advanced persistent threats (APTs).",
     "explanation": "Many advanced persistent threats (APTs) are attributed to nation-state actors, who use cyberattacks to conduct espionage, disrupt critical infrastructure, or influence geopolitical events."},
    
    {"fact": "The U.S. Cyber Command works to protect national interests in cyberspace.",
     "explanation": "The U.S. Cyber Command is responsible for defending the nation's interests in cyberspace, protecting critical infrastructure, and conducting offensive cyber operations when necessary."},
    
    {"fact": "Governments often hire ethical hackers to bolster national security.",
     "explanation": "Governments employ ethical hackers to identify vulnerabilities in national defense systems and critical infrastructure. These experts help strengthen cybersecurity and prevent potential cyberattacks."},
    
    {"fact": "Espionage campaigns often target defense contractors.",
     "explanation": "Cyber espionage campaigns often focus on defense contractors, seeking to steal sensitive information related to national security and military operations."},
    
    {"fact": "The SolarWinds attack was attributed to a Russian-linked APT group.",
     "explanation": "The SolarWinds attack was a sophisticated cyber espionage campaign that affected thousands of organizations globally. It was attributed to a Russian-linked advanced persistent threat (APT) group."},
    
    {"fact": "Cyberattacks on government systems have increased by 95% since 2020.",
     "explanation": "Cyberattacks targeting government systems have increased by 95% since 2020, as adversaries exploit vulnerabilities in public sector infrastructure and services."},
    
    {"fact": "NATO recognizes cyberattacks as potential triggers for collective defense.",
     "explanation": "NATO now recognizes cyberattacks as a potential trigger for collective defense, meaning that an attack on one member state’s cyberspace can invoke Article 5 of the NATO treaty, which calls for mutual defense."},
    
    {"fact": "National cybersecurity strategies are critical for protecting critical infrastructure.",
     "explanation": "National cybersecurity strategies are essential for protecting critical infrastructure, ensuring that government systems, utilities, and communication networks remain secure and operational in the face of growing cyber threats."},
    
    {"fact": "By 2030, AI is expected to dominate cybersecurity solutions.",
     "explanation": "By 2030, artificial intelligence (AI) is expected to be a dominant force in cybersecurity, providing advanced threat detection, automated response, and real-time protection against emerging threats."},
    
    {"fact": "Quantum encryption could redefine secure communication.",
     "explanation": "Quantum encryption has the potential to redefine secure communication by using the principles of quantum mechanics to create virtually unbreakable encryption, safeguarding sensitive information from future threats."},
    
    {"fact": "Cybersecurity spending is projected to reach $300 billion by 2026.",
     "explanation": "Cybersecurity spending is expected to reach $300 billion by 2026, driven by the growing demand for better protection against increasingly sophisticated cyber threats."},
    
    {"fact": "Blockchain-based identity systems may replace traditional logins.",
     "explanation": "Blockchain-based identity systems could replace traditional login methods, providing more secure and private authentication processes that are resistant to fraud and hacking."},
    
    {"fact": "Space cybersecurity will become vital as satellite reliance grows.",
     "explanation": "As the reliance on satellites for communication, navigation, and other services increases, space cybersecurity will become critical to protect these assets from cyberattacks and interference."},
    
    {"fact": "Cybersecurity mesh architecture (CSMA) offers integrated security solutions.",
     "explanation": "Cybersecurity mesh architecture (CSMA) is an integrated approach to security that provides more flexible, scalable, and efficient protection across an organization's network and infrastructure."},
    
    {"fact": "Biometric data security will be a growing concern.",
     "explanation": "As biometric systems like fingerprint and facial recognition become more widespread, securing biometric data will become a growing concern to protect users’ privacy and prevent identity theft."},
    
    {"fact": "The Internet of Behavior (IoB) could raise significant privacy challenges.",
     "explanation": "The Internet of Behavior (IoB) refers to the use of data from IoT devices to influence user behavior. This could raise significant privacy challenges as organizations collect and analyze increasingly personal data."},
    
    {"fact": "Privacy-enhancing technologies (PETs) are becoming more critical.",
     "explanation": "Privacy-enhancing technologies (PETs) are gaining importance as organizations seek to balance user privacy with the need for data analytics, protecting sensitive information while still deriving value from data."},
    
    {"fact": "Continuous adaptive risk and trust assessment (CARTA) will redefine cybersecurity frameworks.",
     "explanation": "Continuous adaptive risk and trust assessment (CARTA) is a new approach to cybersecurity that focuses on continuously evaluating risks and trust levels, adapting defenses as needed to address evolving threats."},

    {"fact": "Penetration testing simulates real-world attacks to identify vulnerabilities.",
     "explanation": "Penetration testing (pen testing) is an authorized simulated cyberattack on a system to identify security weaknesses. These tests are crucial in finding vulnerabilities before hackers can exploit them, including unpatched software and weak configurations."},
    {"fact": "Network sniffing tools like Wireshark capture data packets.",
     "explanation": "Wireshark and similar tools enable cybersecurity professionals to capture and analyze data packets traveling through a network. These packets can contain sensitive information such as passwords or session tokens, which attackers could use if intercepted."},
    {"fact": "A buffer overflow occurs when a program writes more data to a block of memory than it can hold.",
     "explanation": "Buffer overflow vulnerabilities allow attackers to overwrite memory, potentially injecting malicious code. This is one of the most common attack vectors in exploiting software vulnerabilities, often used to take control of a system."},
    {"fact": "Cross-Site Scripting (XSS) allows attackers to inject malicious scripts into web applications.",
     "explanation": "XSS is a vulnerability that allows attackers to inject malicious scripts into websites, which then execute in the context of users' browsers. This can be used to steal session cookies, redirect users to malicious websites, or perform actions on behalf of users."},
    {"fact": "SQL injection is a technique used to exploit web application vulnerabilities.",
     "explanation": "SQL injection attacks target web applications by inserting malicious SQL code into input fields. These attacks can manipulate database queries to reveal sensitive information, delete records, or even take control of the database server."},
    {"fact": "Ethical hackers use reconnaissance to gather information on their targets.",
     "explanation": "Reconnaissance is the first step in ethical hacking or penetration testing, where attackers gather information about the target system, such as domain names, email addresses, and open ports. This helps to identify potential vulnerabilities and attack vectors."},
    {"fact": "A firewall helps filter and monitor incoming and outgoing network traffic.",
     "explanation": "Firewalls are critical in network security by acting as a barrier between a trusted internal network and untrusted external networks, like the internet. They filter out malicious traffic based on defined security rules and prevent unauthorized access."},
    {"fact": "Ransomware encrypts data and demands payment for its decryption.",
     "explanation": "Ransomware is a type of malware that encrypts a victim's files and demands a ransom payment for the decryption key. These attacks can cripple businesses, causing significant financial and reputational damage."},
    {"fact": "Social engineering manipulates individuals into divulging confidential information.",
     "explanation": "Social engineering attacks, such as phishing, rely on psychological manipulation to trick individuals into revealing sensitive data, like passwords or financial information. These attacks exploit human trust rather than technical vulnerabilities."},
    {"fact": "Man-in-the-middle (MITM) attacks intercept and alter communication between two parties.",
     "explanation": "MITM attacks involve intercepting communications between two parties, allowing attackers to eavesdrop on sensitive data or modify the messages being sent. These attacks can be mitigated by using encryption protocols such as SSL/TLS."},
    {"fact": "Credential stuffing attacks use leaked credentials to gain unauthorized access.",
     "explanation": "Credential stuffing attacks exploit the reuse of usernames and passwords across multiple websites. Attackers use automated tools to try large lists of stolen credentials to gain access to various accounts."},
    {"fact": "Two-factor authentication (2FA) significantly improves account security.",
     "explanation": "2FA requires two forms of verification: something you know (like a password) and something you have (like a smartphone app or hardware token). This makes it harder for attackers to gain access, even if they know the password."},
    {"fact": "Zero-day vulnerabilities are undiscovered weaknesses that attackers exploit.",
     "explanation": "A zero-day vulnerability is a flaw in software or hardware that has not been discovered or patched by the vendor. Attackers exploit these vulnerabilities before the developer has time to issue a fix, making them highly dangerous."},
    {"fact": "Rootkits allow attackers to maintain privileged access to a system.",
     "explanation": "Rootkits are malicious software designed to hide the presence of other malware on a system. They allow attackers to maintain administrative control over a compromised machine, often remaining undetected for extended periods."},
    {"fact": "A Distributed Denial-of-Service (DDoS) attack floods a network with traffic to make it unavailable.",
     "explanation": "DDoS attacks overwhelm a target server or network with excessive traffic, rendering it unusable. These attacks are often launched using a botnet, a network of infected devices that can be controlled remotely by an attacker."},
    {"fact": "Vulnerability scanners automate the process of identifying security flaws in systems.",
     "explanation": "Vulnerability scanners are automated tools that scan systems for known security weaknesses. These tools help security professionals identify vulnerabilities in their software, network configurations, and infrastructure before they can be exploited."},
    {"fact": "Data loss prevention (DLP) tools help prevent unauthorized sharing of sensitive information.",
     "explanation": "DLP software monitors and controls the movement of sensitive data, preventing it from being sent outside the organization’s network. It can block the transmission of personal data, intellectual property, or confidential information."},
    {"fact": "Sandboxing isolates potentially harmful software in a controlled environment.",
     "explanation": "Sandboxing involves running untrusted software in an isolated environment where it cannot access critical system resources. This technique helps detect malicious behavior without risking damage to the host system."},
    {"fact": "API security ensures that application interfaces are protected from exploitation.",
     "explanation": "API security focuses on protecting the application programming interfaces (APIs) that allow systems to communicate. Weak or poorly designed APIs can be exploited to access data, disrupt services, or execute unauthorized actions."},
    {"fact": "A security information and event management (SIEM) system analyzes and aggregates security data.",
     "explanation": "SIEM systems aggregate and analyze log data from various security devices and systems. They provide real-time analysis of security alerts and help organizations detect and respond to potential threats more effectively."},
    {"fact": "Botnets are networks of infected devices controlled by cybercriminals.",
     "explanation": "A botnet is a collection of internet-connected devices, such as computers, IoT devices, and smartphones, that have been infected with malware and can be controlled remotely by cybercriminals to launch attacks like DDoS or spread ransomware."},
    {"fact": "Code injection attacks manipulate a system's behavior by inserting malicious code.",
     "explanation": "Code injection involves inserting malicious code into an application’s source code to change its execution. Common types include SQL injection, OS command injection, and script injection."},
    {"fact": "Threat hunting is the proactive search for potential cyber threats in a network.",
     "explanation": "Threat hunting is an active and manual approach to identifying signs of cyber threats in a network. Unlike automated security systems, threat hunting relies on skilled cybersecurity professionals searching for subtle indicators of compromise."},
    {"fact": "Encryption is the process of converting data into a secure format.",
     "explanation": "Encryption transforms data into a scrambled format that can only be decrypted with the correct key. This is essential for protecting sensitive data during storage and transmission, ensuring confidentiality and integrity."},
    {"fact": "DNS spoofing redirects users to malicious websites by altering DNS records.",
     "explanation": "DNS spoofing (also known as DNS cache poisoning) involves corrupting the DNS resolver cache to redirect users to malicious websites, potentially stealing personal information or spreading malware."},
    {"fact": "Keylogging records every keystroke typed by the user.",
     "explanation": "Keyloggers are types of spyware that monitor and record every keystroke typed on a device. They are often used in cyberattacks to steal login credentials, credit card information, and other sensitive data."},
    {"fact": "Honeypots are decoy systems used to lure cybercriminals into revealing their tactics.",
     "explanation": "Honeypots are systems designed to look vulnerable and attract cybercriminals. Once attackers interact with them, security professionals can study their tactics and tools to better understand how to defend against real attacks."},
    {"fact": "Encryption keys should be stored securely to avoid unauthorized access.",
     "explanation": "If encryption keys are stored insecurely, attackers can access encrypted data. Best practices for key management include using hardware security modules (HSMs) and ensuring keys are never hard-coded into source code."},
    {"fact": "The principle of least privilege minimizes user access to only what is necessary.",
     "explanation": "The principle of least privilege (PoLP) restricts user permissions to the minimum required for their job. This limits the potential damage if an account is compromised and reduces the attack surface of a system."},
    {"fact": "Security patches are updates that fix vulnerabilities in software or systems.",
     "explanation": "Security patches are vital for protecting systems from new threats. They fix known vulnerabilities that attackers can exploit. Failing to apply security patches in a timely manner leaves systems open to attack."},
    {"fact": "Cloud security is critical for protecting data and services hosted in the cloud.",
     "explanation": "Cloud security involves securing data, applications, and services hosted in cloud environments. As organizations increasingly move to the cloud, ensuring proper security measures are in place is essential for protecting sensitive information."},
    {"fact": "Public-key cryptography enables secure communication over insecure channels.",
     "explanation": "Public-key cryptography uses two keys: a public key for encryption and a private key for decryption. This system allows secure communication even over untrusted networks, like the internet."},
    {"fact": "RSA is one of the most widely used public-key cryptosystems.",
     "explanation": "The RSA algorithm is based on the mathematical difficulty of factoring large numbers. It is widely used for secure data transmission, including in digital signatures and SSL certificates."},
    {"fact": "AES (Advanced Encryption Standard) is the most widely used symmetric encryption algorithm.",
     "explanation": "AES is a symmetric encryption algorithm, meaning it uses the same key for both encryption and decryption. It's used globally to secure data in applications such as VPNs, file encryption, and secure communications."},
    {"fact": "The Diffie-Hellman key exchange allows two parties to securely share a secret key over an insecure channel.",
     "explanation": "The Diffie-Hellman key exchange uses mathematical algorithms to allow two parties to agree on a shared secret key, which can then be used to encrypt future communication."},
    {"fact": "Elliptic Curve Cryptography (ECC) provides the same security as RSA with shorter key lengths.",
     "explanation": "ECC is a form of public-key cryptography based on the algebraic structure of elliptic curves. It provides strong security while using smaller keys, which improves efficiency compared to traditional methods like RSA."},
    {"fact": "Symmetric encryption uses the same key for both encryption and decryption.",
     "explanation": "Symmetric encryption is faster and more efficient than asymmetric encryption because it uses a single key for both the encryption and decryption process. However, secure key exchange is a challenge in symmetric cryptography."},
    {"fact": "Hash functions are used to produce fixed-length outputs (hashes) from variable-length input data.",
     "explanation": "Hash functions take any input (like a file or a password) and generate a fixed-length output. These are commonly used for data integrity checks and storing password hashes securely."},
    {"fact": "SHA-256 is a cryptographic hash function that produces a 256-bit hash value.",
     "explanation": "SHA-256 is part of the SHA-2 family of hash functions and is widely used in blockchain technology, digital signatures, and certificate authorities for ensuring data integrity."},
    {"fact": "A digital signature verifies the authenticity and integrity of a message.",
     "explanation": "Digital signatures use asymmetric cryptography to authenticate the sender's identity and ensure that the message has not been altered during transmission. It works by signing data with a private key and verifying it with the sender’s public key."},
    {"fact": "Perfect forward secrecy (PFS) ensures that session keys are not compromised even if the private key is later exposed.",
     "explanation": "PFS ensures that each session has a unique key, making past communications secure even if an attacker eventually gains access to the server's private key. This is crucial in maintaining long-term security."},
    {"fact": "The Caesar cipher is one of the earliest known encryption techniques.",
     "explanation": "The Caesar cipher is a type of substitution cipher where each letter in the plaintext is shifted by a fixed number. Although very simple, it demonstrates the basic concept of encryption."},
    {"fact": "Quantum cryptography is based on the principles of quantum mechanics and provides theoretically unbreakable encryption.",
     "explanation": "Quantum cryptography uses the behavior of quantum particles to securely exchange keys and encrypt information. The security is based on the fact that any attempt to observe quantum data will disturb it, thus revealing any eavesdropping."},
    {"fact": "The RSA algorithm's security relies on the difficulty of factoring large prime numbers.",
     "explanation": "RSA encryption relies on the fact that factoring large composite numbers into prime factors is computationally difficult. This makes it one of the strongest encryption methods currently available."},
    {"fact": "Cryptanalysis is the study of breaking cryptographic systems.",
     "explanation": "Cryptanalysis involves examining cryptographic algorithms and systems to find weaknesses that can be exploited to break the encryption. It's a crucial area of cybersecurity, as it helps identify vulnerabilities in systems."},
    {"fact": "A one-time pad is a theoretically unbreakable encryption system.",
     "explanation": "The one-time pad uses a key that is as long as the message and is used only once. If the key is truly random and kept secret, the encryption is mathematically proven to be unbreakable."},
    {"fact": "Digital certificates are used to verify the identity of an entity in digital communications.",
     "explanation": "Digital certificates, issued by Certificate Authorities (CAs), verify the identity of websites, organizations, or individuals, ensuring that their communication is secure and trusted."},
    {"fact": "SSL/TLS protocols use public-key cryptography to secure web communications.",
     "explanation": "SSL/TLS protocols use asymmetric cryptography to exchange a session key for symmetric encryption, ensuring secure communication between web servers and browsers. SSL/TLS is essential for HTTPS websites."},
    {"fact": "HMAC (Hash-based Message Authentication Code) combines a cryptographic hash function with a secret key for data integrity and authentication.",
     "explanation": "HMAC uses both a cryptographic hash function (like SHA-256) and a secret key to create a unique message authentication code. It provides both data integrity and authentication for the message sender."},
    {"fact": "Quantum key distribution (QKD) uses quantum mechanics to securely distribute cryptographic keys.",
     "explanation": "QKD uses the principles of quantum mechanics to distribute cryptographic keys securely. If a third party tries to intercept the key, the quantum state is altered, alerting both the sender and receiver."},
    {"fact": "Blowfish is a symmetric block cipher that uses a variable-length key for encryption.",
     "explanation": "Blowfish is a fast and flexible encryption algorithm that supports keys of varying lengths, from 32 to 448 bits. It’s often used in applications like VPNs and disk encryption."},
    {"fact": "Triple DES (3DES) applies the DES algorithm three times to increase security.",
     "explanation": "Triple DES (3DES) applies the outdated DES encryption algorithm three times with different keys to enhance security. While more secure than DES, it is less efficient than modern algorithms like AES."},
    {"fact": "The ElGamal encryption system is based on the Diffie-Hellman key exchange and provides semantic security.",
     "explanation": "ElGamal encryption, based on the Diffie-Hellman key exchange, provides secure encryption of messages in a way that ensures the encryption is semantically secure, meaning an attacker cannot gain any useful information from the ciphertext."},
    {"fact": "The birthday paradox is used in cryptography to understand the likelihood of a collision in hash functions.",
     "explanation": "The birthday paradox suggests that the probability of two random inputs producing the same hash value (a collision) is higher than expected. This concept is used to test the strength of hash functions against collisions."},
    {"fact": "Ciphertext is the encrypted form of the original plaintext data.",
     "explanation": "Ciphertext is the result of applying an encryption algorithm to plaintext data. It appears random and unreadable without the corresponding decryption key."},
    {"fact": "The Diffie-Hellman protocol is vulnerable to man-in-the-middle (MITM) attacks without authentication.",
     "explanation": "While Diffie-Hellman allows two parties to securely agree on a secret key, it is vulnerable to MITM attacks if the identity of the parties is not authenticated beforehand. Without authentication, an attacker could intercept and modify the exchanged keys."},
    {"fact": "Salting passwords adds a random value to the password before hashing to prevent rainbow table attacks.",
     "explanation": "Salting involves adding a random value (salt) to a password before hashing it. This makes it much harder for attackers to use precomputed hash tables (rainbow tables) to crack passwords."},
    {"fact": "AES-256 is considered the gold standard in symmetric encryption.",
     "explanation": "AES-256 is a 256-bit version of the AES encryption algorithm. It’s widely regarded as the gold standard for secure encryption due to its robustness and resistance to brute-force attacks."},
    {"fact": "A cryptographic nonce is a random number used only once to ensure uniqueness in cryptographic protocols.",
     "explanation": "A nonce is used in cryptographic systems to ensure that certain values (like encryption keys or session identifiers) are not reused, preventing replay attacks and ensuring the security of the communication."},
    {"fact": "Elliptic curve Diffie-Hellman (ECDH) is a variant of the Diffie-Hellman key exchange using elliptic curve cryptography.",
     "explanation": "ECDH is a variant of the Diffie-Hellman key exchange algorithm that uses elliptic curves to generate keys. It provides the same level of security as traditional Diffie-Hellman with smaller keys, making it more efficient."},
    {"fact": "Quantum computers threaten traditional cryptographic algorithms like RSA and ECC.",
     "explanation": "Quantum computers have the potential to break widely used cryptographic systems, including RSA and ECC, by efficiently solving the mathematical problems these systems rely on (like factoring large numbers and solving discrete logarithms)."},
    {"fact": "Firewalls are used to control incoming and outgoing network traffic based on predetermined security rules.",
     "explanation": "A firewall acts as a barrier between a trusted internal network and untrusted external networks, monitoring and controlling traffic based on rules defined by the administrator."},
    {"fact": "Intrusion Detection Systems (IDS) monitor network traffic for signs of malicious activity.",
     "explanation": "An IDS analyzes network traffic and alerts administrators to potential threats, such as malware or unauthorized access attempts."},
    {"fact": "Virtual Private Networks (VPNs) encrypt internet traffic to provide secure connections over public networks.",
     "explanation": "VPNs encrypt data sent over the internet, making it unreadable to hackers or anyone else trying to intercept it. VPNs are widely used for secure remote access."},
    {"fact": "A Denial of Service (DoS) attack floods a network with traffic to overwhelm resources and make services unavailable.",
     "explanation": "In a DoS attack, the attacker sends massive amounts of data or requests to a server, preventing legitimate users from accessing the targeted service or network."},
    {"fact": "Network segmentation divides a network into smaller sub-networks to enhance security.",
     "explanation": "Segmenting a network creates isolated zones, limiting access to sensitive data or systems and reducing the attack surface in the event of a breach."},
    {"fact": "A Zero Trust Architecture (ZTA) assumes that every request, both inside and outside the network, should be verified before access is granted.",
     "explanation": "Zero Trust security eliminates the traditional idea of a trusted internal network and focuses on verifying every user and device regardless of their location."},
    {"fact": "Deep Packet Inspection (DPI) analyzes the content of data packets for malicious threats or vulnerabilities.",
     "explanation": "DPI goes beyond simple packet filtering by examining the actual content of data packets, allowing for more thorough detection of potential threats and malicious activities."},
    {"fact": "Network Access Control (NAC) enforces security policies on devices attempting to connect to the network.",
     "explanation": "NAC systems ensure that devices meet predefined security standards, like up-to-date antivirus software, before they can access the network, reducing the risk of threats."},
    {"fact": "Multi-factor authentication (MFA) adds an extra layer of security by requiring multiple forms of verification.",
     "explanation": "MFA requires users to authenticate their identity using multiple methods, such as something they know (password), something they have (smartphone), and something they are (fingerprint)." },
    {"fact": "Port scanning tools are used to discover open ports on a network, helping security professionals identify vulnerabilities.",
     "explanation": "Port scanning involves probing a network to find open ports that could potentially be exploited by attackers, allowing administrators to secure them."},
    {"fact": "A man-in-the-middle (MITM) attack occurs when an attacker secretly intercepts and potentially alters communication between two parties.",
     "explanation": "MITM attacks can be used to eavesdrop on sensitive communications or even modify data in transit, making them highly dangerous in network security."},
    {"fact": "Network traffic analysis can help identify unusual patterns or anomalies that may indicate an attack or compromise.",
     "explanation": "By constantly monitoring network traffic, security professionals can detect abnormal activities that could signal potential cyber threats, allowing for faster response."},
    {"fact": "A Demilitarized Zone (DMZ) is a network segment designed to isolate publicly accessible services from an internal network.",
     "explanation": "The DMZ allows web servers, email servers, and other public-facing resources to be isolated from the rest of the internal network, reducing the risk of an internal breach."},
    {"fact": "Encryption is used to protect data in transit and at rest from unauthorized access.",
     "explanation": "Encryption transforms data into an unreadable format, ensuring that even if an attacker intercepts the data, they cannot decipher it without the decryption key."},
    {"fact": "A Security Information and Event Management (SIEM) system collects and analyzes security data from across the network.",
     "explanation": "SIEM systems provide real-time monitoring, reporting, and analysis of security events, helping to detect, understand, and respond to network security threats."},
    {"fact": "The Border Gateway Protocol (BGP) is used to exchange routing information between networks but is vulnerable to attacks.",
     "explanation": "BGP is essential for routing traffic on the internet, but its lack of built-in security mechanisms makes it susceptible to attacks like route hijacking and data interception."},
    {"fact": "A Distributed Denial of Service (DDoS) attack amplifies a DoS attack by using multiple systems to flood the target network with traffic.",
     "explanation": "DDoS attacks are more devastating than regular DoS attacks because they utilize a large botnet of compromised devices to generate massive traffic that overwhelms network resources."},
    {"fact": "Rogue DHCP servers can assign incorrect IP addresses to devices on a network, redirecting traffic and potentially allowing attackers to intercept data.",
     "explanation": "A rogue DHCP server provides incorrect IP addresses to devices on the network, potentially causing devices to be misdirected or enabling attackers to intercept traffic."},
    {"fact": "Network Address Translation (NAT) hides internal IP addresses by mapping them to a single public IP address.",
     "explanation": "NAT allows multiple devices within an internal network to share a single public IP address, providing privacy and security by obscuring internal network addresses from external observers."},
    {"fact": "A network-based firewall filters traffic based on IP addresses, ports, and protocols to protect a network from unauthorized access.",
     "explanation": "Network firewalls examine the packets passing through them, blocking or allowing traffic based on security rules related to IP addresses, ports, and protocols."},
    {"fact": "Endpoint security refers to protecting individual devices on the network, such as laptops, smartphones, and workstations.",
     "explanation": "Endpoint security tools protect devices by enforcing security policies, scanning for malware, and providing other protective measures to prevent compromise and data theft."},
    {"fact": "A VPN concentrator is a device that creates and manages multiple VPN connections, allowing secure access to a network from remote locations.",
     "explanation": "VPN concentrators provide a scalable way to securely manage multiple remote VPN connections, ensuring that users can safely access a corporate network from anywhere."},
    {"fact": "Packet sniffers can intercept and log network traffic to help diagnose issues and detect malicious activities.",
     "explanation": "Packet sniffers are tools used to monitor and capture data packets moving across the network. While they can be helpful for troubleshooting, they can also be exploited by attackers to steal sensitive data."},
    {"fact": "DNS security extensions (DNSSEC) add layers of security to the Domain Name System (DNS) to protect against spoofing and cache poisoning.",
     "explanation": "DNSSEC ensures that the responses to DNS queries are authentic and have not been tampered with, preventing attackers from redirecting traffic to malicious websites."},
    {"fact": "Intrusion Prevention Systems (IPS) actively block malicious activities in real-time, whereas IDS only detects and alerts.",
     "explanation": "An IPS goes one step further than an IDS by not only detecting potential threats but also actively preventing them from causing harm by blocking malicious traffic."},
    {"fact": "MAC filtering can restrict access to a network based on the unique MAC addresses of devices.",
     "explanation": "MAC address filtering allows network administrators to control which devices can connect to the network by only allowing devices with specific, approved MAC addresses."},
    {"fact": "Application layer firewalls filter traffic based on specific applications or services to ensure security at a deeper level.",
     "explanation": "Unlike traditional firewalls that work at lower levels of the network stack, application layer firewalls inspect the actual application data, helping protect against more sophisticated attacks targeting specific services."},
    {"fact": "A honeypot is a decoy system or resource used to lure attackers and detect their methods and intentions.",
     "explanation": "Honeypots are intentionally vulnerable systems set up to attract attackers. They allow security professionals to study attack strategies, methods, and tools without risking valuable data."},
    {"fact": "The Open Web Application Security Project (OWASP) provides guidelines for securing web applications against common vulnerabilities.",
     "explanation": "OWASP is a nonprofit organization that focuses on improving web application security. They provide a list of the most critical web application security risks, such as SQL injection and cross-site scripting."},
    {"fact": "A VLAN (Virtual Local Area Network) can isolate traffic between different groups of users within the same physical network.",
     "explanation": "VLANs allow for logical segmentation of a network, reducing the size of broadcast domains and improving security by isolating traffic between different network segments."},
    {"fact": "A network security policy defines the rules and practices that regulate network access and usage.",
     "explanation": "Network security policies are critical in ensuring that all users and devices follow the organization's security standards, outlining acceptable use, threat response procedures, and access controls."},
    {"fact": "An IPsec VPN secures network communications by encrypting IP packets between two devices.",
     "explanation": "IPsec is a set of protocols used to secure IP communications. It ensures confidentiality, integrity, and authenticity of the data sent between devices by encrypting IP packets."},
    {"fact": "Bandwidth throttling is used to limit the speed of network traffic, typically for performance optimization or during security events.",
     "explanation": "Bandwidth throttling restricts the amount of data transferred at a given time, which can be useful for network management or mitigating DDoS attacks by limiting traffic flow."},
    {"fact": "A SQL injection attack targets vulnerabilities in database-driven web applications by injecting malicious SQL code into input fields.",
     "explanation": "SQL injection is a technique used by attackers to exploit improper sanitization of user input in web applications, allowing them to access, modify, or delete database information."},
    {"fact": "Cybersecurity awareness training helps employees identify phishing attacks, social engineering, and other malicious activities.",
     "explanation": "Security training teaches employees about the latest threats and how to recognize suspicious activity, significantly reducing the risk of human error that could lead to a breach."},
    {"fact": "Network segmentation and micro-segmentation help minimize the impact of a breach by isolating critical systems and data.",
     "explanation": "Segmentation divides the network into smaller sections to limit an attacker's ability to move laterally. Micro-segmentation goes further by applying security policies at a more granular level."},
    {"fact": "A vulnerability scanner helps identify security flaws in systems and networks before attackers can exploit them.",
     "explanation": "Vulnerability scanners assess systems and networks for weaknesses, providing administrators with insights into potential security gaps that need to be addressed."},
    {"fact": "The role of a network administrator is critical in ensuring that network devices are updated with the latest security patches.",
     "explanation": "Keeping network devices, such as routers and firewalls, updated with the latest patches is essential for protecting against vulnerabilities that could be exploited by attackers."},
    {"fact": "Network Time Protocol (NTP) is used to synchronize the clocks of computers over a network, but it can also be a target for DDoS amplification attacks.",
     "explanation": "NTP is commonly used for time synchronization, but attackers can exploit it for amplification in DDoS attacks, flooding a target with a high volume of traffic."},
    {"fact": "A security audit helps identify gaps in an organization's security posture and ensure compliance with industry standards.",
     "explanation": "Security audits involve a thorough examination of an organization's systems and policies to identify vulnerabilities and verify compliance with relevant security regulations and best practices."},
]




# Track the index of the last fact shown
if "fact_index" not in st.session_state:
    st.session_state.fact_index = 0

# List of fun names with roles
names = {
    "Cyber Hero 👑": "Penetration Tester",
    "Cyber Guardian 🛡️": "Security Analyst",
    "Cyber Defender 🛡️": "Incident Responder"
}

# Welcome message with a fun conversation
st.title("Cybersecurity Facts Tool")
st.write("Hey, **cyber hero**! 👋 Ready to learn some cool (and scary) cybersecurity facts? Let’s dive in! But first, what's your name? Choose one below!")

# Create a button for each name option
name_choice = st.radio("Pick your cyber identity:", list(names.keys()))

# Display the role based on choice
st.write(f"Ah, so you’re a **{names[name_choice]}**! 🤩 Let's get started, shall we?")

# Show the current fact and explanation
if st.button('Next Fact'):
    # Ensure we skip repeated facts
    fact_choice = facts[st.session_state.fact_index]
    st.write(f"**Fact #{st.session_state.fact_index + 1}:** {fact_choice['fact']}")
    st.write(f"**Explanation:** {fact_choice['explanation']}")

    # Increment the index, and reset if we’ve reached the end of the facts list
    st.session_state.fact_index += 1
    if st.session_state.fact_index >= len(facts):
        # Congratulate the user when they finish all facts
        st.write(f"🎉 Congratulations, **{name_choice}**, you’ve completed all the facts! You’re officially a **Cyber Hero**! 👑💙")
        st.session_state.fact_index = 0  # Reset to start again
        st.write("Press 'Next Fact' to start again and become even more of a legend! 🚀")
else:
    st.write("Press the button to see the first cybersecurity fact and its explanation!!!")

# Option to get more facts in order
st.write("If you want to know more, just press 'Next Fact' to move through each fact one by one! 💙")

import streamlit as st
import random
import time

# 30 Cybersecurity facts and explanations
facts = [
    {"fact": "A system that monitors and controls incoming and outgoing network traffic.", "answer": "firewall", "explanation": "A firewall is a network security system that monitors and controls incoming and outgoing network traffic to prevent unauthorized access."},
    {"fact": "A type of attack where many systems flood a target with traffic.", "answer": "DDoS attack", "explanation": "A Distributed Denial of Service (DDoS) attack floods a target system with massive traffic, causing it to slow down or crash."},
     {"fact": "A secure connection used to access a remote network safely.", "answer": "VPN", "explanation": "A VPN (Virtual Private Network) provides secure, encrypted access to remote networks over the internet."},
    {"fact": "A decoy system designed to lure attackers for study.", "answer": "honeypot", "explanation": "A honeypot is a security mechanism used to attract and trap cyber attackers to study their methods."},
    {"fact": "A technique where attackers insert malicious code into an input field.", "answer": "SQL injection", "explanation": "SQL injection is an attack where attackers insert harmful SQL code into input fields to manipulate a website's database."},
    {"fact": "A system used to detect suspicious network activity.", "answer": "IDS", "explanation": "Intrusion Detection Systems (IDS) monitor network traffic for unusual patterns and alert administrators to potential threats."},
    {"fact": "An attack that involves trying all possible passwords until the correct one is found.", "answer": "brute-force attack", "explanation": "A brute-force attack attempts all possible combinations of passwords until the correct one is found."},
    {"fact": "A cryptographic protocol used to secure internet communication.", "answer": "SSL", "explanation": "Secure Sockets Layer (SSL) is a cryptographic protocol that encrypts data transferred between web servers and browsers."},
    {"fact": "An attack that exploits an unknown vulnerability in software.", "answer": "zero-day exploit", "explanation": "A zero-day exploit takes advantage of an unknown vulnerability in software, before developers can patch it."},
    {"fact": "A type of scam where attackers pretend to be someone trustworthy to steal information.", "answer": "phishing attack", "explanation": "Phishing attacks involve cybercriminals impersonating trusted entities to trick victims into revealing sensitive information."},
    {"fact": "Malicious software designed to damage or gain unauthorized access to computer systems.", "answer": "malware", "explanation": "Malware is software designed to harm or gain unauthorized access to systems, including viruses, worms, and trojans."},
    {"fact": "A security protocol used to protect online communication.", "answer": "TLS", "explanation": "Transport Layer Security (TLS) is used to secure communication over the internet by encrypting data."},
    {"fact": "A prolonged and targeted cyberattack aimed at stealing data or compromising systems.", "answer": "APT", "explanation": "Advanced Persistent Threats (APTs) are long-term, targeted cyberattacks designed to steal data or infiltrate systems."},
    {"fact": "Simulated cyberattacks to identify vulnerabilities in a system before exploitation.", "answer": "penetration testing", "explanation": "Penetration testing simulates attacks to identify vulnerabilities in systems before malicious actors can exploit them."},
    {"fact": "The process of converting data into a secure, unreadable format.", "answer": "encryption", "explanation": "Encryption converts readable data into a scrambled format to prevent unauthorized access."},
    {"fact": "A method requiring more than one form of verification to access a system.", "answer": "multi-factor authentication", "explanation": "Multi-factor authentication (MFA) requires more than one form of verification to ensure a user's identity."},
    {"fact": "A network of infected computers controlled by a cybercriminal.", "answer": "botnet", "explanation": "A botnet is a network of compromised devices controlled remotely by cybercriminals to carry out malicious activities."},
    {"fact": "A method used to verify the authenticity and integrity of a document.", "answer": "digital signature", "explanation": "A digital signature authenticates the sender and ensures the document's integrity by using encryption."},
    {"fact": "A feature that prevents traffic from leaking if the VPN connection drops.", "answer": "VPN kill switch", "explanation": "A VPN kill switch blocks internet traffic if the VPN connection drops, preventing data leaks."},
    {"fact": "The act of manipulating people into revealing confidential information.", "answer": "social engineering", "explanation": "Social engineering tricks people into divulging confidential information by exploiting their trust."},
    {"fact": "The three core principles of cybersecurity: confidentiality, integrity, and availability.", "answer": "CIA triad", "explanation": "The CIA triad represents the core principles of cybersecurity: confidentiality, integrity, and availability."},
    {"fact": "Malicious software that encrypts a victim's data and demands a ransom.", "answer": "ransomware", "explanation": "Ransomware encrypts a victim’s data and demands a ransom for the decryption key."},
    {"fact": "A deceptive technique where attackers impersonate legitimate websites to steal user credentials.", "answer": "spoofing", "explanation": "Spoofing tricks victims into thinking they are on legitimate sites or interacting with trusted entities."},
    {"fact": "A cryptographic hash function used to secure sensitive data.", "answer": "SHA", "explanation": "Secure Hash Algorithm (SHA) is used for hashing sensitive data for integrity verification."},
    {"fact": "A unique identifier for your device on a network.", "answer": "IP address", "explanation": "An IP address uniquely identifies devices on a network to enable communication."},
    {"fact": "The process of verifying someone's identity before granting access.", "answer": "authentication", "explanation": "Authentication ensures only authorized users can access sensitive data or systems."},
    {"fact": "A software tool that scans for vulnerabilities in a network.", "answer": "vulnerability scanner", "explanation": "Vulnerability scanners help identify weaknesses in networks or systems before attackers exploit them."},
    {"fact": "A malicious software disguised as legitimate software.", "answer": "trojan horse", "explanation": "A Trojan horse appears to be a legitimate program but performs malicious actions when executed."},
    {"fact": "An attack that intercepts and relays communications between two parties.", "answer": "man-in-the-middle attack", "explanation": "A man-in-the-middle attack intercepts communications between two parties, often to steal sensitive data."},
    {"fact": "A unique, randomly generated code used to verify the authenticity of a transaction.", "answer": "OTP", "explanation": "A one-time password (OTP) is a temporary code used to authenticate users and secure transactions."}
]

# Initialize session state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0
    st.session_state.score = 0
    st.session_state.start_time = None
    st.session_state.answer_given = False

# Function to get current flashcard
def get_current_fact():
    return facts[st.session_state.card_index]

# Timer check function
def time_up(start_time):
    elapsed_time = time.time() - start_time
    return elapsed_time >= 60  # 60 seconds limit to answer

# Check if answers are close (case-insensitive, strips spaces)
def is_answer_correct(user_answer, correct_answer):
    user_answer = user_answer.strip().lower()
    correct_answer = correct_answer.strip().lower()
    return user_answer == correct_answer

# Game Interface
st.title("Cybersecurity Flashcard Game 🕹️")
st.write("Welcome, **Cyber Hero**! Ready to prove your skills in cybersecurity? Let's start with a challenge!")

# Player's name input
player_name = st.text_input("Enter your name, Cyber Hero:")
if player_name:
    st.session_state.player_name = player_name
    st.write(f"Hey, **{player_name}**, let's go! 🔥")

# Get current flashcard
fact_choice = get_current_fact()

# Flashcard styling with animation and detailed explanation
st.markdown("""
    <style>
    @keyframes sway {
        0% { transform: rotate(0deg); }
        50% { transform: rotate(5deg); }
        100% { transform: rotate(0deg); }
    }
    .card {
        background-color: #003366;
        color: white;
        padding: 50px;
        border-radius: 20px;
        font-size: 24px;
        box-shadow: 3px 5px 10px rgba(0,0,0,0.5);
        border: 5px solid #333333; /* Black Velvet border */
        width: 500px; /* Big square card */
        margin: 0 auto;
        animation: sway 1s ease-in-out infinite;
    }
    </style>
""", unsafe_allow_html=True)

# Show question (front of the card)
st.markdown(f'<div class="card">**Fact #{st.session_state.card_index + 1}:** {fact_choice["fact"]}</div>', unsafe_allow_html=True)

# Start timer if it isn't already
if st.session_state.start_time is None:
    st.session_state.start_time = time.time()

# Timer countdown
time_left = max(0, 60 - int(time.time() - st.session_state.start_time))
st.write(f"⏳ Time Left: {time_left}s")

# Player inputs their answer
user_answer = st.text_input("What's your answer?", key="answer_input")

# Button to check the answer
if not st.session_state.answer_given:
    if st.button("Check Answer"):
        # Check answer and feedback
        if is_answer_correct(user_answer, fact_choice["answer"]):
            st.session_state.score += 1
            st.success(f"Correct! 💥 {fact_choice['answer']} is right! {fact_choice['explanation']}")
        else:
            st.error(f"Oops! The correct answer was **{fact_choice['answer']}**. {fact_choice['explanation']}")
        st.session_state.answer_given = True

# Button to move to next flashcard
if st.session_state.answer_given and st.button("Next Flashcard"):
    if st.session_state.card_index < len(facts) - 1:
        st.session_state.card_index += 1
        st.session_state.start_time = time.time()
        st.session_state.answer_given = False
    else:
        st.write(f"Game Over! Your Score: {st.session_state.score}/{len(facts)}")
        if st.session_state.score == len(facts):
            st.success("You are a Cyber Hero! 🏆")
        elif st.session_state.score >= 10:
            st.success("Not bad! Keep learning! 🎓")
        else:
            st.write("Better luck next time, Cyber Hero! 💪")

# Display current score
st.write(f"Your current score: {st.session_state.score}")


