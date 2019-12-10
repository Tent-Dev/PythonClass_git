--page1
select ProductName, UnitPrice, UnitsInStock from Products;

--page2
select ProductName, UnitPrice as Price, UnitsInStock from Products;

--page3
select ProductName, UnitPrice as Price, UnitsInStock, (UnitPrice*UnitsInStock) as ValueInStock from Products;

--page4
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products;

--page5
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products
ORDER by ValueInStock DESC;

--page6
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products
where valueInStock >= 3000
ORDER by ValueInStock DESC;

--page7
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products
where valueInStock >= 3000 and valueInStock<100
ORDER by ValueInStock DESC;

--page8
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products
WHERE UnitsInStock in (0,10,20)
Order by UnitsInStock desc , ProductName ASC;

--page9
select upper(ProductName), UnitPrice as Price , UnitsInStock, UnitPrice*UnitsInStock as ValueInStock
from Products
WHERE UnitsInStock between 10 and 20
Order by UnitsInStock desc , ProductName ASC;

--page10
select companyname, contactname,country, city, Fax from Suppliers;

--page11
select companyname, contactname,country, city, Fax from Suppliers
where lower(country) = 'usa';

--page12
select companyname, contactname,country, city, Fax from Suppliers
where lower(country) = 'usa' and Fax isnull ;

--page13
select companyname, contactname,country, city, Fax from Suppliers
where country like 's%' ;

--page14
select companyname, contactname,country, city, Fax from Suppliers
where country like '%a' ;

--page15
select companyname, contactname,country, city, Fax from Suppliers
where country like '%an%' ;

--page16
select companyname, contactname,country, city, Fax from Suppliers
where country like '__an%' ;

--page17
select companyname, contactname,country, city, Fax from Suppliers
where country like '%land' ;

--page18
select TitleOfCourtesy,  FirstName, Lastname, BirthDate from Employees;

--page19
select TitleOfCourtesy || FirstName || " " || Lastname as Emp, BirthDate from Employees;

--page20
select TitleOfCourtesy || FirstName || " " || Lastname as Emp, BirthDate from Employees
order by BirthDate desc;

--page21
select TitleOfCourtesy || FirstName || " " || Lastname as Emp, BirthDate from Employees
where BirthDate like '1995%'
order by BirthDate desc;

--page22
select TitleOfCourtesy || FirstName || " " || Lastname as Emp, BirthDate from Employees
where BirthDate like '____-01%'
order by BirthDate desc;

--page23
select productname, CompanyName as SupplierCompanyName from Products
join Suppliers
on Products.supplierID = Suppliers.supplierID;

--page24
select productname, CompanyName as SupplierCompanyName, CategoryName from Products
join Suppliers, Categories
on Products.supplierID = Suppliers.supplierID and Products.CategoryId = Categories.CategoryID;

--page25
CREATE VIEW infoView as 
select o.OrderID,  o.OrderDate, c.CompanyName, (e.TitleOfCourtesy || " " || e.Firstname || " " || e.Lastname) as 'Employee', s.CompanyName from Orders o
join Customers c
on o.CustomerId = c.CustomerID 
join Employees e
on o.EmployeeID = e.EmployeeId
join Shippers s
on o.ShipVia = s.ShipperID;

SELECT * FROM infoView;

--page26
select count(ProductID), sum(UnitPrice), max(UnitPrice) as MaxUnitPrice,  min(UnitPrice) as MinUnitPrice, avg(UnitPrice) as AverageOfUnitPrice from Products;

--page27
select CategoryName , count(ProductID) as NoOfProduct from Categories
join Products
on Categories.CategoryID = Products.CategoryId
group by CategoryName;

--page28
select CategoryName , count(ProductID) as NoOfProduct from Categories
join Products
on Categories.CategoryID = Products.CategoryId
group by CategoryName
order by NoOfProduct DESC;

--page29
select CategoryName , count(ProductID) as NoOfProduct from Categories
join Products
on Categories.CategoryID = Products.CategoryId
group by CategoryName
having NoOfProduct < 10
order by NoOfProduct DESC;

--page30
INSERT INTO Categories (CategoryName)
VALUES ('catename1');
INSERT INTO Categories (CategoryName, Description)
VALUES ('catename2', 'desc2');

--page31
UPDATE Categories
SET Description = 'desc3'
WHERE CategoryID = 11;

--page32
DELETE FROM Categories WHERE CategoryID=11;