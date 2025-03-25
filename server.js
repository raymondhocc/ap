import express from 'express';
import cors from 'cors';
import { format, subDays } from 'date-fns';

const app = express();
app.use(cors());
app.use(express.json());

// Mock data
const payments = [
  {
    id: 1,
    referenceNumber: 'PAY-2023-001',
    amount: 1500.00,
    paymentDate: format(subDays(new Date(), 2), 'yyyy-MM-dd'),
    paymentMethod: 'bank_transfer',
    status: 'completed',
    notes: 'Monthly service payment',
    vendorId: 1
  },
  {
    id: 2,
    referenceNumber: 'PAY-2023-002',
    amount: 2300.00,
    paymentDate: format(subDays(new Date(), 5), 'yyyy-MM-dd'),
    paymentMethod: 'check',
    status: 'pending',
    notes: 'Office supplies',
    vendorId: 2
  },
  {
    id: 3,
    referenceNumber: 'PAY-2023-003',
    amount: 5000.00,
    paymentDate: format(subDays(new Date(), 10), 'yyyy-MM-dd'),
    paymentMethod: 'bank_transfer',
    status: 'completed',
    notes: 'Software license renewal',
    vendorId: 3
  }
];

const vendors = [
  {
    id: 1,
    name: 'Tech Solutions Inc',
    email: 'billing@techsolutions.com',
    phone: '555-0101'
  },
  {
    id: 2,
    name: 'Office Supplies Co',
    email: 'accounts@officesupplies.com',
    phone: '555-0102'
  },
  {
    id: 3,
    name: 'Software Services Ltd',
    email: 'billing@softwareservices.com',
    phone: '555-0103'
  }
];

const invoices = [
  {
    id: 1,
    invoiceNumber: 'INV-2023-001',
    amount: 1500.00,
    vendorId: 1,
    status: 'paid'
  },
  {
    id: 2,
    invoiceNumber: 'INV-2023-002',
    amount: 2300.00,
    vendorId: 2,
    status: 'pending'
  },
  {
    id: 3,
    invoiceNumber: 'INV-2023-003',
    amount: 5000.00,
    vendorId: 3,
    status: 'paid'
  }
];

// API endpoints
app.get('/api/payments', (req, res) => {
  res.json(payments);
});

app.post('/api/payments', (req, res) => {
  const newPayment = {
    id: payments.length + 1,
    ...req.body,
    createdAt: new Date().toISOString()
  };
  payments.push(newPayment);
  res.status(201).json(newPayment);
});

app.patch('/api/payments/:id', (req, res) => {
  const { id } = req.params;
  const paymentIndex = payments.findIndex(p => p.id === parseInt(id));
  if (paymentIndex === -1) {
    return res.status(404).json({ error: 'Payment not found' });
  }
  payments[paymentIndex] = { ...payments[paymentIndex], ...req.body };
  res.json(payments[paymentIndex]);
});

app.get('/api/vendors', (req, res) => {
  res.json(vendors);
});

app.get('/api/invoices', (req, res) => {
  res.json(invoices);
});

const PORT = 3003;
app.listen(PORT, () => {
  console.log(`Mock API server running on port ${PORT}`);
});
