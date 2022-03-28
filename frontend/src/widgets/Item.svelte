<script>
	export let wname;
	export let jdPrice;
	export let originalImgUrl, longImgUrl;
	export let good, reviews;
	export let spuId;
	let url = "https://some_upstream_url/" + spuId + ".html";
</script>

	<div class="section">
		<div class="card is-horizontal columns">
			<div class="card-image column is-one-fifths">
				<figure class="image is-square">
					<img src={longImgUrl} >
				</figure>
			</div>
			<div class="card-content column is-four-fifths">
				<div class="media-content">
					<a href="{url}" target="_blank"><p class="title is-4">{wname}</p></a>
					<p class="subtitle is-6"><b>￥</b>{jdPrice}</p>
				</div>
				<div class="content">
					<p>
						<span>{good}</span>
						<span>{reviews}</span>
					</p>
				</div>
			</div>
		</div>
	</div>

<style>
	.card:hover {
		z-index: 555555 !important;
	}
</style>
