<template>
  <svg class="icon">
    <use :xlink:href="`#${icon}`" />
  </svg>
</template>

<script>
export default {
  name: 'SvgIcon',
  props: {
    icon: {
      type: String,
      required: true
    }
  }
}
</script>

<style scoped>
svg.icon {
  fill: currentColor;
  height: 24px;
  width: 24px;
  margin-bottom: 0.125em;
  vertical-align: middle;
}
</style>
