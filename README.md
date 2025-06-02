<p align="center">
   <img src="https://github.com/user-attachments/assets/7d564981-cb81-43e7-819a-25ffcfc5bd72" width=40% height=40%/>
</p>

# HBnB - UML

## 📘 Project Overview

**HBnB - UML** is the first phase of the HBnB Evolution project, focused on creating a comprehensive **technical blueprint** for a simplified AirBnB-like application. This phase involves the design and documentation of the architecture, business logic, and data flow of the system using **UML diagrams** and clear technical explanations.

---

## 🧠 Objective

The goal is to produce a complete technical documentation package that will guide future development stages. It includes high-level and low-level design diagrams, business rules, and sequence flows that illustrate the interaction between system components.

---

## 📌 Problem Description

The application will allow users to:

- 👤 **Manage users**: Register, update profiles, and distinguish between regular users and administrators.
- 🏠 **Manage places**: Create, update, and delete listings with details such as title, description, price, and location.
- ✍️ **Manage reviews**: Leave reviews with ratings and comments on places visited.
- 🛠️ **Manage amenities**: Create and associate amenities with places.

Each object will be uniquely identifiable via an `ID`, and all entities will track creation and update timestamps for audit purposes.

---

## 🧱 Business Entities & Requirements

### 👤 User
- `first_name`, `last_name`, `email`, `password`
- `is_admin` (boolean)
- CRUD operations: register, update, delete

### 🏠 Place
- `title`, `description`, `price`, `latitude`, `longitude`
- Belongs to a User
- Can have many Amenities
- CRUD operations

### ✍️ Review
- `rating`, `comment`
- Associated with one User and one Place
- CRUD operations by place

### 🛠️ Amenity
- `name`, `description`
- CRUD operations
- Can be associated with multiple Places

---

## 🧱 Architecture

The application follows a **three-layer architecture**:

1. **Presentation Layer**: APIs and services for user interaction
2. **Business Logic Layer**: Models and core logic
3. **Persistence Layer**: Data storage (to be implemented in Part 3)

Communication between layers uses the **facade pattern** to encapsulate and decouple logic.

---

## ✅ Deliverables

### 1. 📦 High-Level Package Diagram
- Illustrates the 3-tier architecture
- Shows interaction between layers via the facade pattern

### 2. 🧩 Class Diagram (Business Logic Layer)
- Includes `User`, `Place`, `Review`, and `Amenity` classes
- Attributes, methods, and relationships
- Focus on Place ↔ Amenity association

### 3. 🔁 Sequence Diagrams (API Calls)
- **User Registration**
- **Place Creation**
- **Review Submission**
- **Place Listing**

Each diagram will show:
- Actors and objects involved
- Method calls and data flow
- Layer interaction (Presentation ↔ Logic ↔ Persistence)

### 4. 📚 Full Technical Document
- All diagrams and explanatory notes compiled into a professional document
- Describes design choices, data flow, and business rule enforcement

---

## 🔧 Constraints

- All diagrams must use **UML standard notation**
- Must reflect **all business rules** outlined above
- Documentation should be **implementation-ready** for future development phases

---

## ✅ Project Files

The repository is structured as follows:

HBnB-UML/  
├── 0. High-Level Package Diagram.md  
├── 1. Detailed Class Diagram for Business Logic Layer.md  
├── 2. Sequence Diagrams for API Calls.md  
└── README.md

---

Each `.md` file contains:

- **0. High-Level Package Diagram**: Overview of system architecture and layer interaction
- **1. Detailed Class Diagram**: UML class diagram covering `User`, `Place`, `Review`, `Amenity`
- **2. Sequence Diagrams**: UML sequence diagrams for key API operations

---

## 🧪 Deliverables

### 📦 High-Level Package Diagram
Describes the layered architecture and facade pattern.

### 🧩 Class Diagram (Business Logic Layer)
Details classes, attributes, methods, and relationships.

### 🔁 Sequence Diagrams
Four key API call diagrams:
- User registration
- Place creation
- Review submission
- Fetching places list

---

## 🔧 Constraints

- All diagrams must use **UML standard notation**
- Business rules must be reflected accurately
- Documentation must be implementation-ready

---

## 🧑‍💻 Contributors

Project developed as part of the **Holberton School curriculum**.

---

## 🧑‍💻 Authors

f-qrm & P-Y74
