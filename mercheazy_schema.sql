--DB CREATION
CREATE TABLE customers(
	customer_id SERIAL PRIMARY KEY,
	customer_name VARCHAR(100) NOT NULL,
	customer_phone VARCHAR(20),
	customer_age INT
);

CREATE TABLE vendors (
    vendor_id SERIAL PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL,
    vendor_phone VARCHAR(20),
    vendor_location VARCHAR(100)
);

CREATE TABLE products (
    product_id SERIAL PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL UNIQUE,
    product_category VARCHAR(50), -- e.g., 'produce', 'dairy', 'cleaning supplies'
    product_brand VARCHAR(50),
    cost_price NUMERIC(10, 2) NOT NULL,
    selling_price NUMERIC(10, 2) NOT NULL
);

CREATE TABLE inventory(
	lot_id SERIAL PRIMARY KEY,
	product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
	vendor_id INT NOT NULL REFERENCES vendors(vendor_id) ON DELETE RESTRICT,
	stock_qty NUMERIC(10, 2) NOT NULL,
    mfg_date DATE,
    exp_date DATE,
	UNIQUE (product_id, vendor_id, mfg_date) 
);

CREATE TABLE orders(
	order_id SERIAL PRIMARY KEY,
	customer_id INT REFERENCES customers(customer_id) ON DELETE SET NULL,
	order_date TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
	payment_mode VARCHAR(20),
	order_status VARCHAR(20) DEFAULT 'Pending'
);

CREATE TABLE order_items(
	order_item_id SERIAL PRIMARY KEY,
	order_id INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
	product_id INT NOT NULL REFERENCES products(product_id) ON DELETE RESTRICT,
	quantity NUMERIC(10, 2) NOT NULL, 
    unit_price NUMERIC(10, 2) NOT NULL, 
    line_total NUMERIC(10, 2) NOT NULL 
);

CREATE INDEX idx_order_items_product ON order_items (product_id);



















