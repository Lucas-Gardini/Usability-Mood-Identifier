import { Server, Socket } from "socket.io";
import chalk from "chalk";

const io = new Server(3000);

let webClient: Socket<any> = null as any;

io.on("connection", (socket) => {
	console.log(chalk.blue("[🐣] Socket conectado"));

	//recebe uma mensagem do cliente
	socket.on("emotion", (...args) => {
		console.log(chalk.blue("[🐣] Emotion recebida"));
		console.log(args);

		if (webClient) webClient.emit("emotion", ...args);
	});

	socket.on("client-connection", (...args) => {
		console.log(chalk.blue("[🐣] Client connection recebida"));
		console.log(args);

		webClient = socket;
	});
});

console.log(chalk.green("[⚡] Socket aberto em 3000"));
