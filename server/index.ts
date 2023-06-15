import { Server, Socket } from "socket.io";
import Express from "express";
import chalk from "chalk";
import http from "http";
import { Low } from "lowdb";
import { JSONFile } from "lowdb/node";

import { join, dirname } from "node:path";
import { fileURLToPath } from "node:url";

// db.json file path
const __dirname = dirname(fileURLToPath(import.meta.url));
const file = join(__dirname, "db.json");

// Configure lowdb to write data to JSON file
const defaultData: { executions: { user: string | null; time: string; emotion: string | null }[] } = { executions: [] };
const adapter = new JSONFile<typeof defaultData>(file);
const db = new Low<typeof defaultData>(adapter, defaultData);

const app = Express();
const server = http.createServer(app);
const io = new Server(server);

app.use(Express.static("website"));

let webClient: Socket<any> = null as any;
let currentUser: string | null = null;

io.on("connection", (socket) => {
	console.log(chalk.blue("[🐣] Socket conectado"));

	//recebe uma mensagem do cliente
	socket.on("emotion", async (...args) => {
		console.log(chalk.blue("[🐣] Emotion recebida"));

		if (webClient) {
			webClient.emit("emotion", ...args);

			db.data.executions.push({
				user: currentUser,
				time: new Date().toLocaleString(),
				emotion: args[0],
			});

			await db.write();
		}
	});

	socket.on("web", async (...args) => {
		console.log(chalk.blue("[🖥️] Interface web connectada"));

		db.data.executions.push({
			user: currentUser,
			time: new Date().toLocaleString(),
			emotion: null,
		});

		await db.write();

		webClient = socket;
	});
});

const port = 3000;

const readline = require("readline").createInterface({
	input: process.stdin,
	output: process.stdout,
});

readline.question("Qual o nome do usuário(a)?", async (name: string) => {
	currentUser = name;
	readline.close();

	await db.read();

	server.listen(port, () => {
		console.log(chalk.green("[⚡] Socket aberto em 3000"));
	});
});
