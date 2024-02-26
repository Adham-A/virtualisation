<script>

export default {
	data() {
		return {

		}
	},
	props: {
		participations: {
			type: Array,
			required: true
		}
	},
}
</script>

<template>
	<div id="table-container">
		<table border=1 frame=hsides rules=rows>
			<thead>
				<tr>
					<th colspan="3">Participations</th>
				</tr>
				<tr>
					<td>Rank</td>
					<td>Player Name2</td>
					<td>Score</td>
				</tr>
			</thead>
			<tbody>
				<tr v-for="(participation, index) in this.participations" :key="index">
					<td>{{ index + 1 }}</td>
					<td>{{ participation.playerName }}</td>
					<td>{{ participation.score }}</td>
				</tr>
			</tbody>
		</table>
	</div>
</template>

<style>
#table-container {
	width: 80%;
	height: 400px;
	overflow-y: auto;
	overflow-x: hidden;
	margin: auto;
}

table {
	width: 100%;
	border-collapse: collapse;
	height: 200px;
	background-color: #63768d;
}

th,
td {
	padding: 10px;
	/* border: 2px solid black;   */
	border-bottom: 1px solid black;
	word-wrap: break-word;
	max-width: 50px;
}
</style>