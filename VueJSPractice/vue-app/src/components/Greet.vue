<template>
    <h2> Hello {{ name }}</h2>
</template>

<script>
export default {
    name: 'Hello',
    props: ['name']
};
</script>

<style scoped>
</style>