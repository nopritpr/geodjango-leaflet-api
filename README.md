# India-Centric Spatial Data Platform

A full-stack web application designed to store, manage, and visualize geospatial point and polygon data. This project features a robust backend REST API developed with Python and Django, connected to a PostGIS database, and an interactive map frontend rendered with Leaflet.js.


<img width="1917" height="968" alt="Screenshot 2025-07-25 123906" src="https://github.com/user-attachments/assets/5dec0f39-978f-4db5-be58-aa6edce81060" />


## Project Overview

This application is a full-stack geospatial data platform architecturally divided into a distinct backend service and a frontend client. It is designed to handle the complete lifecycle of geographic data, from its persistence in a database to its final visualization in a web browser.

**System Architecture:**

-   **Database Layer**: Utilizes PostgreSQL with the PostGIS extension, providing a robust, spatially-aware data store optimized for geographic queries and data types (points, polygons).
-   **Backend Service**: A backend built with Django and its GeoDjango module. It handles all business logic, data modeling via the ORM, and serves as the primary interface to the database.
-   **API Layer**: Implemented using Django REST Framework (DRF), it exposes a set of RESTful endpoints. The API serializes database models into the standard GeoJSON format for interoperability with mapping clients.
-   **Frontend Client**: A lightweight, single-page application built with HTML, CSS, and JavaScript. It uses the Leaflet.js library to consume data from the backend API and render it on an interactive map.

## Core Features

-   **RESTful API**: Full CRUD (Create, Read, Update, Delete) functionality for both point and polygon data types.
-   **Spatial Database Integration**: Leverages the power of PostGIS for efficient, spatially-indexed data storage.
-   **GeoJSON Compliant**: The API serves data in the standard GeoJSON format, ensuring compatibility with a wide range of mapping tools and libraries.
-   **Interactive Map Frontend**: A powerful map visualization using Leaflet.js that dynamically fetches and displays all data from the API.
-   **Layer Controls**: The map interface includes controls to toggle data layers (Points, Polygons) and switch between different base maps (e.g., Streets and Satellite).

## Technology Stack

| Category      | Technology                                           | Purpose                                                    |
|---------------|------------------------------------------------------|------------------------------------------------------------|
| **Backend**   | Python 3.12, Django 5.2                              | Core application logic and web framework.                  |
| **Database**  | PostgreSQL + PostGIS                                 | Robust, open-source relational and spatial database.       |
| **API**       | Django REST Framework, DRF-GIS                       | Building the REST API and serializing data to GeoJSON.     |
| **GIS Library**| GDAL (via OSGeo4W)                                   | The core geospatial data library that GeoDjango depends on. |
| **Frontend**  | HTML, CSS, JavaScript, Leaflet.js                    | Creating the interactive map visualization.                |
| **CORS**      | `django-cors-headers`                                | Securely handles requests between the frontend and backend servers. |

## Showcase & Results

Here are screenshots demonstrating the key components of the running application.

#### Interactive Map Frontend
<img width="765" height="729" alt="Screenshot 2025-07-25 121336" src="https://github.com/user-attachments/assets/391dafe2-c8ad-4519-8a8a-ed12ad304758" />



#### Browsable API

<img width="991" height="860" alt="Screenshot 2025-07-25 165512" src="https://github.com/user-attachments/assets/1d2e9c81-d9d1-4c39-ab2c-91a6efa981f4" />
<img width="964" height="745" alt="Screenshot 2025-07-25 165528" src="https://github.com/user-attachments/assets/96d0fc89-07de-4026-9e24-8b24c4a94a0d" />


Prerequisites
Ensure you have the following installed on your system:
-   Python 3.12+
-   PostgreSQL (with the PostGIS extension installed via Stack Builder)
-   OSGeo4W (with the `GDAL` package selected during installation)
-   Git

