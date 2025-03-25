# Accounts Payable Management System

A modern web application for managing accounts payable, built with React and Vite. Features a responsive UI with real-time updates, interactive charts, and comprehensive financial reporting.

## Features

### 1. Dashboard
- Overview of accounts payable status
- Key financial metrics at a glance
- Recent activity tracking
- Quick action buttons for common tasks

### 2. Vendor Management
- Add and manage vendor profiles
- Track vendor payment history
- Vendor contact information storage
- Vendor-specific payment terms

### 3. Invoice Processing
- Create and manage invoices
- Track outstanding balances
- Monitor overdue payments
- Invoice status tracking
- Payment scheduling

### 4. Payment Management
- Process payments with multiple payment methods
- Real-time payment status updates
- Interactive payment history table
- Bulk payment processing
- Payment filtering and search
- Modal-based payment creation
- Status-based payment management

### 5. Financial Reports
- Interactive charts and visualizations
- Monthly payment trends analysis
- Top vendor payment analysis
- Payment method distribution
- Downloadable financial reports
- Custom date range selection
- Real-time data updates

## Technical Stack

### Frontend
- React 18.2.0
- React Router DOM 6.15.0
- Recharts 2.10.3 (for data visualization)
- date-fns 4.1.0 (for date handling)
- Tailwind CSS 3.3.6 (for styling)
- Vite 4.4.5 (for build tooling)

### Backend
- Express.js 4.18.2
- CORS middleware
- RESTful API architecture

## Getting Started

### Prerequisites
- Node.js (Latest LTS version recommended)
- npm or yarn package manager

### Installation

1. Clone the repository:
```bash
git clone [repository-url]
```

2. Install dependencies:
```bash
npm install
```

3. Start the API server (runs on port 3003):
```bash
npm run server
```

4. In a new terminal, start the development server (runs on port 3002):
```bash
npm run dev
```

The application will be available at `http://localhost:3002`

### API Endpoints

The backend server provides the following endpoints:

- GET `/api/payments` - Retrieve all payments
- POST `/api/payments` - Create a new payment
- PATCH `/api/payments/:id` - Update payment status
- GET `/api/vendors` - Retrieve all vendors
- GET `/api/invoices` - Retrieve all invoices

### Building for Production

To create a production build:
```bash
npm run build
```

To preview the production build:
```bash
npm run preview
```

## Project Structure

```
accounts-payable/
├── src/
│   ├── components/          # Reusable UI components
│   │   ├── Dashboard.jsx   # Main dashboard component
│   │   ├── Payments.jsx    # Payment management
│   │   ├── Reports.jsx     # Financial reporting
│   │   ├── Vendors.jsx     # Vendor management
│   │   └── Invoices.jsx    # Invoice processing
│   ├── App.jsx             # Main application component
│   ├── main.jsx           # Application entry point
│   └── App.css            # Global styles
├── server.js              # API server
├── public/               # Static assets
├── index.html           # HTML entry point
└── package.json         # Project dependencies and scripts
```

## Key Components

### App.jsx
The main application component that handles:
- Routing configuration
- Layout structure
- Navigation menus
- Quick action widgets
- Activity tracking

### Payments.jsx
Comprehensive payment management featuring:
- Payment creation modal
- Payment status updates
- Interactive data table
- Search and filtering
- Error handling
- Loading states

### Reports.jsx
Advanced financial reporting with:
- Interactive charts (Line, Bar, Pie)
- Data analysis tools
- Report downloads
- Date range selection
- Real-time updates

## Development Guidelines

### Running the Application
1. Start the API server first: `npm run server`
2. Start the development server: `npm run dev`
3. Both servers must be running for full functionality

### Making Changes
1. Frontend changes hot-reload automatically
2. API changes require server restart
3. Use the browser console to monitor API interactions
4. Check the Network tab for request/response data

### Common Issues
- If the API server fails to start, check if port 3003 is in use
- If the dev server fails to start, check if port 3002 is in use
- Ensure all API endpoints return proper JSON responses
- Verify CORS settings if experiencing API connection issues

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
