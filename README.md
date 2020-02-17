# DABAC (Dynamic Attribute Based Access Control): a Machine Learning Enhanced Access Control for Big Data

Access Controls (AC) are one of the main means of defence in IT systems, unfortunately, Big Data Systems are still lacking in this field, the current well-known  ACs are vulnerable and can be compromised because of policy misconfiguration and lack of contextuality. In this article we propose a Machine Learning approach to optimize ABAC (Attribute Based Access Control) with the aim to reduce the attacks that are overlooked by the hardcoded policies (i.e: users abusing their privileges). We use unsupervised learning outlier detection algorithms to detect anomalous user behaviors. The Framework was implemented in Python and its performance tested using the UNSW-NB15 Data Set.

# Implementation:

To implement our framework, we used the Python language, the ABAC component was based on [VAKT](https://github.com/kolotaev/vakt) , an attribute based access control toolkit coded in Python, we modified it and added our Machine Learning component then tuned it’s decision process to include the feedback from the said component.
The added Outlier Detection component is in the folder **/Outlier/**
The final decision is made by the **Guard** Component, it is the main entry point to make a decision. It has one method `is_allowed` that takes an Inquiry as an input, and returns a boolean answer: is it allowed or not.
