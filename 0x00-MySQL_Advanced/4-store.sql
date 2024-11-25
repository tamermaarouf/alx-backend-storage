-- Write a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.

CREATE TRIGGER dec_quantity
AFTER
INSERT ON orders
FOR EACH ROW BEGIN UPDATE items
	SET items.quantity = items.quantity-NEW.number
	WHERE items.name = NEW.item_name;
