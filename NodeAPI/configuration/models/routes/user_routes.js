module.exports = app => {

const customers = require("../controllers/user.controller.js");

  // Create a new Customer
  app.post("/user", user.create);

  // Retrieve all Customers
  app.get("/user", user.findAll);

  // Retrieve a single Customer with customerId
  app.get("/user/:userId", user.findOne);

  // Update a Customer with customerId
  app.put("/user/:userId", user.update);

  // Delete a Customer with customerId
  app.delete("/user/:userId", user.delete);

  // Create a new Customer
  app.delete("/user", user.deleteAll);
};