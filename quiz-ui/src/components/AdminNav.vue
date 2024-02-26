<script>
export default {
	name: "AdminNav",

}
</script>

<template> 
	<div id="side-navbar">
		<nav class="position-absolute d-flex flex-column justify-content-center">
			<router-link to="/admin-page">Admin Home</router-link>
			<router-link to="/question-list-page">Question List Page</router-link>
		</nav>
	</div>
</template>

<style scoped>
#side-navbar {
	background-color: #7da6f5;
	border: 1px solid #7da6f5;
	width: 220px;
	height: 440px;
	border-radius: 25px;
	padding: 10px;
}

</style>