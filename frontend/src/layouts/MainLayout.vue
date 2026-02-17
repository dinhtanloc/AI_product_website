<template>
	<div class="min-h-screen bg-gradient-to-br from-gray-50 to-blue-100 flex flex-col">
		<header class="bg-white shadow-md py-4 px-8 flex items-center justify-between">
			<h1 class="text-2xl font-bold text-blue-700 tracking-wide">Assistant System</h1>
			<slot name="header-actions"></slot>
		</header>
		<main class="flex-1 flex flex-col items-center justify-center p-6">
			<slot />
		</main>
	</div>
</template>
