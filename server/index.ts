import { Server } from "socket.io";
import chalk from "chalk";

const io = new Server(3000);

io.on("connection", (socket) => {
	// Envia uma messagem para o cliente
	socket.emit("hello from server", 1, "2", { 3: Buffer.from([4]) });

	//recebe uma mensagem do cliente
	socket.on("hello from client", (...args) => {
		// ...
	});
});

console.log(chalk.green("[⚡] Socket aberto em 3000"));
