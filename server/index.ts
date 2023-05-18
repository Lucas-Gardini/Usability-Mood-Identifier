import { Server, Socket } from "socket.io";
import Express from "express";
import chalk from "chalk";
import http from "http";

const app = Express();
const server = http.createServer(app);
const io = new Server(server);

app.use(Express.static("website"));

let webClient: Socket<any> = null as any;

io.on("connection", (socket) => {
	console.log(chalk.blue("[🐣] Socket conectado"));

	//recebe uma mensagem do cliente
	socket.on("emotion", (...args) => {
		console.log(chalk.blue("[🐣] Emotion recebida"));

		if (webClient) webClient.emit("emotion", ...args);
	});

	socket.on("web", (...args) => {
		console.log(chalk.blue("[🖥️] Interface web connectada"));

		webClient = socket;
	});
});

// Start the server
const port = 3000;
server.listen(port, () => {
	console.log(chalk.green("[⚡] Socket aberto em 3000"));
});
