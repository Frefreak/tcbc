<script>
	import "bulma";
	import { search } from '../api';
	import Item from '../widgets/Item.svelte';
	
	let keyword = '';
	let infos = [];

async function do_search(kw) {
	let r = await search(kw);
	infos = r.info;
}

</script>
<svelte:head>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css" integrity="sha512-iBBXm8fW90+nuLcSKlbmrPcLa0OT92xO1BIsZ+ywDWZCvqsWgccV3gFoRBv0z+8dLJgyAHIhR35VZc2oM/gI1w==" crossorigin="anonymous" referrerpolicy="no-referrer" />
</svelte:head>

<div class="container">
	<div class="box">
		<div class="field has-addons">
			<div class="control has-icons-left is-expanded">
				<input type="text" placeholder="keyword" bind:value={keyword} class="input is-info" />
				<span class="icon is-left">
					<i class="fas fa-search-plus"></i>
				</span>
			</div>
			<div class="control">
				<button type=button class="button is-primary" on:click="{do_search(keyword)}">Search!</button>
			</div>
		</div>
	</div>
	<div class="box">
		{#if infos.length > 0}
			{#each infos as info}
				<Item {...info} />
			{/each}
		{:else}
			<p>no result</p>
		{/if}
	</div>
</div>

<style>
</style>
