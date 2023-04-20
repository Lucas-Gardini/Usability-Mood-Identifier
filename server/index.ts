import { Server } from "socket.io";
import chalk from "chalk";

const io = new Server(3000);

io.on("connection", (socket) => {
	console.log(chalk.blue("[🐣] Socket conectado"));

	//recebe uma mensagem do cliente
	socket.on("hello from client", (...args) => {
		// ...
	});
});

console.log(chalk.green("[⚡] Socket aberto em 3000"));
