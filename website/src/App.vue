<script setup>
import { io } from "socket.io-client";

import Dialog from "primevue/dialog";
import Button from "primevue/button";

import { ref, onMounted } from "vue";

const visible = ref(false);

const socket = io("http://localhost:3000", { path: "/" });

onMounted(() => {
	socket.connect();

	socket.on("connect", () => {
		alert("Connected to server");
		socket.value.send("client-connection", "Hello from client");
	});
});
</script>

<template>
	<div class="card flex justify-content-center">
		<Dialog v-model:visible="visible" modal header="Header" :style="{ width: '50vw' }">
			<p>
				Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
				minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
				reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
				culpa qui officia deserunt mollit anim id est laborum.
			</p>
			<template #footer>
				<Button label="No" icon="pi pi-times" @click="visible = false" text />
				<Button label="Yes" icon="pi pi-check" @click="visible = false" autofocus />
			</template>
		</Dialog>
	</div>
</template>
