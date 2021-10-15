const mysql = require("mysql");
const dbConfig = require("Users/mpa.comm/Desktop/NodeMySQL_API/application/configuration/mysqldb_config.js");


const connection = mysql.connector({
  host: dbConfig.HOST,
  user: dbConfig.USER,
  password: dbConfig.PASSWORD,
  database: dbConfig.DB
});


connection.connect(error => {
  if (error) throw error;
  console.log("Successfully connected to the database.");
});

module.exports = connection;