import { io } from "https://cdn.socket.io/4.4.1/socket.io.esm.min.js";

const socket = io("http://localhost:3000");

socket.on("connect", () => {
	console.log("Conectado");

	socket.emit("web", "Hello Server");
});

socket.on("disconnect", () => {
	console.log("Desconectado");
});

//Definir com socket
const emotions = {
	neutral: {
		backgroundColor: "rgba(128, 128, 128, 0.2)",
		color: "black",
		fontSize: "12px",
	},
	happy: {
		backgroundColor: "rgba(255, 255, 0, 0.2)",
		color: "black",
		fontSize: "16px",
	},
	sad: {
		backgroundColor: "rgba(0, 0, 255, 0.2)",
		color: "white",
		fontSize: "14px",
	},
	angry: {
		backgroundColor: "rgba(255, 0, 0, 0.2)",
		color: "white",
		fontSize: "18px",
	},
	confused: {
		backgroundColor: "rgba(128, 0, 128, 0.2)",
		color: "white",
		fontSize: "14px",
	},
	fear: {
		backgroundColor: "rgba(0, 0, 0, 0.2)",
		color: "white",
		fontSize: "12px",
	},
	surprise: {
		backgroundColor: "rgba(255, 0, 255, 0.2)",
		color: "black",
		fontSize: "16px",
	},
};

let emocao = Object.keys(emotions)[0];

socket.on("emotion", (message) => {
	console.log(message);
	emocao = message;

	aplicarEstilos();
	alterarBody();
	alterarTamanho();
});

function aplicarEstilos() {
	let elements = document.querySelectorAll("div, p, ion-icon");

	console.log(emocao);

	for (let i = 0; i < elements.length; i++) {
		let element = elements[i];

		element.style.color = emotions[emocao].backgroundColor;
	}
}

function alterarTamanho() {
	let elements = document.querySelectorAll("input, p");
	// let button = document.querySelectorAll("button");

	for (let i = 0; i < elements.length; i++) {
		let element = elements[i];

		element.style.fontSize = emotions[emocao].fontSize;
	}
}

function alterarBody() {
	let body = document.querySelectorAll("body");

	body[0].style.backgroundColor = emotions[emocao].backgroundColor;
}

alterarBody();
aplicarEstilos();
alterarTamanho();

const accordionBtn = document.querySelectorAll("[data-accordion-btn]");
const accordion = document.querySelectorAll("[data-accordion]");

for (let i = 0; i < accordionBtn.length; i++) {
	accordionBtn[i].addEventListener("click", function () {
		const clickedBtn = this.nextElementSibling.classList.contains("active");

		for (let i = 0; i < accordion.length; i++) {
			if (clickedBtn) break;

			if (accordion[i].classList.contains("active")) {
				accordion[i].classList.remove("active");
				accordionBtn[i].classList.remove("active");
			}
		}

		this.nextElementSibling.classList.toggle("active");
		this.classList.toggle("active");
	});
}
