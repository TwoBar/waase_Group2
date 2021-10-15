const sql = require("./database.js");


// constructor
const User = function(user) {
    this.first_name = user.firstname;
    this.last_name = user.lastname;
    this.email = user.email;
    this.password = user.password;
    this.last_updated= user.lastupdated;
  };
  
  User.create = (newUser, result) => {
    sql.query("INSERT INTO user SET ?", newUser, (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(err, null);
        return;
      }
  
      console.log("created user: ", { Id: res.insertId, ...newUser });
      result(null, { Id: res.insertId, ...newUser });
    });
  };
  
  User.findById = (userId, result) => {
    sql.query(`SELECT * FROM user WHERE id = ${userId}`, (err, res) => {
      if (err) {
        console.log("error: ", err);
        result(err, null);
        return;
      }
  
      if (res.length) {
        console.log("found user: ", res[0]);
        result(null, res[0]);
        return;
      }

    result({ kind: "not_found" }, null);
});
};

User.getAll = result => {
sql.query("SELECT * FROM user", (err, res) => {
  if (err) {
    console.log("error: ", err);
    result(null, err);
    return;
  }

  console.log("user: ", res);
  result(null, res);
});
};

User.updateById = (id, user, result) => {
sql.query(
  "UPDATE user SET firstname = ?, lastname = ?, email =?, password =?, last_updated = ?, WHERE id = ?",
  [user.firstname, user.lastname, user.email, user.password , last_updated, id],
  (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found Customer with the id
      result({ kind: "not_found" }, null);
      return;
    }

    console.log("updated : ", { id: id, ...customer });
      result(null, { id: id, ...customer });
    }
  );
};

User.remove = (id, result) => {
  sql.query("DELETE FROM user WHERE id = ?", id, (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    if (res.affectedRows == 0) {
      // not found Customer with the id
      result({ kind: "not_found" }, null);
      return;
    }

    console.log("deleted customer with id: ", id);
    result(null, res);
  });
};

User.removeAll = result => {
  sql.query("DELETE FROM user", (err, res) => {
    if (err) {
      console.log("error: ", err);
      result(null, err);
      return;
    }

    console.log(`deleted ${res.affectedRows} user`);
    result(null, res);
  });
};

module.exports = User;