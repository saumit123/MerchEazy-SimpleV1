-- Insert Customers
INSERT INTO customers (customer_name, customer_phone, customer_age) VALUES
('Rajesh Kumar', '+91-9876543210', 35),
('Priya Sharma', '+91-9876543211', 28),
('Amit Patel', '+91-9876543212', 42),
('Sneha Gupta', '+91-9876543213', 31),
('Vikram Singh', '+91-9876543214', 45),
('Anita Reddy', '+91-9876543215', 38),
('Rahul Verma', '+91-9876543216', 29),
('Kavita Joshi', '+91-9876543217', 33),
('Suresh Nair', '+91-9876543218', 51),
('Deepa Iyer', '+91-9876543219', 27);

-- Insert Vendors
INSERT INTO vendors (vendor_name, vendor_phone, vendor_location) VALUES
('Fresh Farms Pvt Ltd', '+91-9123456780', 'Delhi'),
('Dairy Delights Co', '+91-9123456781', 'Amul, Gujarat'),
('Green Valley Produce', '+91-9123456782', 'Punjab'),
('Ocean Fresh Suppliers', '+91-9123456783', 'Mumbai'),
('Spice Garden Traders', '+91-9123456784', 'Kerala'),
('Grain Masters', '+91-9123456785', 'Haryana'),
('Beverage Distributors Inc', '+91-9123456786', 'Bangalore'),
('Hygiene Products Ltd', '+91-9123456787', 'Chennai'),
('Snack World Wholesale', '+91-9123456788', 'Pune'),
('Bakery Essentials', '+91-9123456789', 'Kolkata');

-- Insert Products (50 items across different categories)
INSERT INTO products (product_name, product_category, product_brand, cost_price, selling_price) VALUES
-- Produce (10 items)
('Fresh Tomatoes 1kg', 'produce', 'Local Farm', 40.00, 60.00),
('Onions 1kg', 'produce', 'Local Farm', 30.00, 45.00),
('Potatoes 1kg', 'produce', 'Local Farm', 25.00, 40.00),
('Green Capsicum', 'produce', 'Fresh Farms', 60.00, 90.00),
('Carrots 500g', 'produce', 'Fresh Farms', 20.00, 35.00),
('Spinach Bunch', 'produce', 'Organic', 15.00, 25.00),
('Bananas Dozen', 'produce', 'Local Farm', 40.00, 60.00),
('Apples 1kg', 'produce', 'Kashmir', 120.00, 180.00),
('Oranges 1kg', 'produce', 'Nagpur', 60.00, 90.00),
('Green Beans 500g', 'produce', 'Fresh Farms', 30.00, 50.00),

-- Dairy (10 items)
('Milk Full Cream 1L', 'dairy', 'Amul', 54.00, 65.00),
('Curd 400g', 'dairy', 'Mother Dairy', 25.00, 35.00),
('Paneer 200g', 'dairy', 'Amul', 80.00, 100.00),
('Butter 100g', 'dairy', 'Amul', 45.00, 55.00),
('Cheese Slices 200g', 'dairy', 'Britannia', 110.00, 140.00),
('Ghee 500ml', 'dairy', 'Amul', 280.00, 340.00),
('Buttermilk 500ml', 'dairy', 'Mother Dairy', 18.00, 25.00),
('Fresh Cream 250ml', 'dairy', 'Amul', 85.00, 110.00),
('Lassi 200ml', 'dairy', 'Mother Dairy', 20.00, 30.00),
('Yogurt 400g', 'dairy', 'Nestle', 40.00, 55.00),

-- Grains & Pulses (10 items)
('Basmati Rice 5kg', 'grains', 'India Gate', 450.00, 550.00),
('Wheat Flour 5kg', 'grains', 'Aashirvaad', 200.00, 250.00),
('Toor Dal 1kg', 'grains', 'Fortune', 110.00, 140.00),
('Moong Dal 1kg', 'grains', 'Fortune', 120.00, 150.00),
('Chana Dal 1kg', 'grains', 'Fortune', 90.00, 120.00),
('Red Kidney Beans 500g', 'grains', 'Tata Sampann', 85.00, 110.00),
('Poha 500g', 'grains', 'Patanjali', 35.00, 50.00),
('Besan 1kg', 'grains', 'Aashirvaad', 75.00, 95.00),
('Suji 500g', 'grains', 'Pillsbury', 30.00, 45.00),
('Oats 1kg', 'grains', 'Quaker', 180.00, 230.00),

-- Beverages (10 items)
('Tea Powder 250g', 'beverages', 'Tata Tea', 110.00, 140.00),
('Coffee Powder 200g', 'beverages', 'Nescafe', 180.00, 220.00),
('Cold Drink 2L', 'beverages', 'Coca Cola', 80.00, 100.00),
('Fruit Juice 1L', 'beverages', 'Real', 95.00, 120.00),
('Mineral Water 1L', 'beverages', 'Bisleri', 15.00, 20.00),
('Energy Drink 250ml', 'beverages', 'Red Bull', 90.00, 120.00),
('Soft Drink 600ml', 'beverages', 'Pepsi', 30.00, 40.00),
('Mango Drink 1L', 'beverages', 'Maaza', 75.00, 95.00),
('Lemon Soda 750ml', 'beverages', 'Sprite', 35.00, 45.00),
('Green Tea Bags 25pcs', 'beverages', 'Lipton', 125.00, 160.00),

-- Cleaning Supplies (10 items)
('Dish Wash Liquid 500ml', 'cleaning supplies', 'Vim', 85.00, 110.00),
('Detergent Powder 1kg', 'cleaning supplies', 'Surf Excel', 150.00, 190.00),
('Floor Cleaner 1L', 'cleaning supplies', 'Lizol', 140.00, 175.00),
('Toilet Cleaner 500ml', 'cleaning supplies', 'Harpic', 95.00, 120.00),
('Hand Wash 250ml', 'cleaning supplies', 'Dettol', 60.00, 80.00),
('Soap Bar 125g', 'cleaning supplies', 'Lux', 30.00, 40.00),
('Glass Cleaner 500ml', 'cleaning supplies', 'Colin', 110.00, 140.00),
('Fabric Softener 1L', 'cleaning supplies', 'Comfort', 180.00, 225.00),
('Bleach 500ml', 'cleaning supplies', 'Domex', 65.00, 85.00),
('All Purpose Wipes', 'cleaning supplies', 'Clorox', 120.00, 155.00);

-- Insert Inventory (linking products with vendors)
INSERT INTO inventory (product_id, vendor_id, stock_qty, mfg_date, exp_date) VALUES
-- Fresh Produce from Fresh Farms and Green Valley
(1, 1, 150.00, '2025-09-28', '2025-10-05'),
(2, 1, 200.00, '2025-09-27', '2025-10-15'),
(3, 1, 180.00, '2025-09-26', '2025-10-20'),
(4, 3, 75.00, '2025-09-29', '2025-10-06'),
(5, 3, 100.00, '2025-09-28', '2025-10-08'),
(6, 3, 50.00, '2025-09-30', '2025-10-03'),
(7, 1, 120.00, '2025-09-29', '2025-10-05'),
(8, 3, 90.00, '2025-09-25', '2025-10-10'),
(9, 1, 110.00, '2025-09-27', '2025-10-08'),
(10, 3, 80.00, '2025-09-29', '2025-10-06'),

-- Dairy Products from Dairy Delights
(11, 2, 200.00, '2025-09-28', '2025-10-05'),
(12, 2, 150.00, '2025-09-29', '2025-10-04'),
(13, 2, 80.00, '2025-09-27', '2025-10-12'),
(14, 2, 100.00, '2025-09-25', '2025-11-25'),
(15, 2, 75.00, '2025-09-26', '2025-11-26'),
(16, 2, 50.00, '2025-09-20', '2026-03-20'),
(17, 2, 120.00, '2025-09-29', '2025-10-06'),
(18, 2, 60.00, '2025-09-28', '2025-10-12'),
(19, 2, 90.00, '2025-09-30', '2025-10-05'),
(20, 2, 100.00, '2025-09-27', '2025-10-10'),

-- Grains from Grain Masters
(21, 6, 100.00, '2025-09-01', '2026-03-01'),
(22, 6, 150.00, '2025-08-15', '2026-02-15'),
(23, 6, 80.00, '2025-09-10', '2026-03-10'),
(24, 6, 70.00, '2025-09-05', '2026-03-05'),
(25, 6, 90.00, '2025-09-12', '2026-03-12'),
(26, 6, 60.00, '2025-09-08', '2026-03-08'),
(27, 6, 100.00, '2025-09-15', '2026-03-15'),
(28, 6, 85.00, '2025-09-18', '2026-03-18'),
(29, 6, 75.00, '2025-09-20', '2026-03-20'),
(30, 6, 50.00, '2025-09-22', '2026-03-22'),

-- Beverages from Beverage Distributors
(31, 7, 120.00, '2025-08-01', '2026-08-01'),
(32, 7, 90.00, '2025-07-15', '2026-07-15'),
(33, 7, 150.00, '2025-09-15', '2025-12-15'),
(34, 7, 100.00, '2025-09-20', '2025-12-20'),
(35, 7, 300.00, '2025-09-25', '2026-09-25'),
(36, 7, 80.00, '2025-09-10', '2026-03-10'),
(37, 7, 180.00, '2025-09-18', '2025-12-18'),
(38, 7, 110.00, '2025-09-22', '2025-12-22'),
(39, 7, 160.00, '2025-09-20', '2025-12-20'),
(40, 7, 100.00, '2025-08-25', '2026-08-25'),

-- Cleaning Supplies from Hygiene Products Ltd
(41, 8, 85.00, '2025-08-01', '2027-08-01'),
(42, 8, 120.00, '2025-07-15', '2027-07-15'),
(43, 8, 95.00, '2025-08-10', '2027-08-10'),
(44, 8, 110.00, '2025-08-05', '2027-08-05'),
(45, 8, 140.00, '2025-07-20', '2027-07-20'),
(46, 8, 200.00, '2025-06-15', '2027-06-15'),
(47, 8, 75.00, '2025-08-12', '2027-08-12'),
(48, 8, 60.00, '2025-08-18', '2027-08-18'),
(49, 8, 90.00, '2025-08-20', '2027-08-20'),
(50, 8, 100.00, '2025-08-22', '2027-08-22');