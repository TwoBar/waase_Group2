module.exports = app => {

const customers = require("");

  
  app.post("/user", user.create);

  
  app.get("/user", user.findAll);

  
  app.get("/user/:userid", user.findOne);

  
  app.put("/user/:userid", user.update);

  
  app.delete("/user/:userid", user.delete);

  
  app.delete("/user", user.deleteAll);
};