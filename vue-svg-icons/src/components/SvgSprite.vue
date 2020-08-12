<template>
  <svg width="0" height="0" style="display:none;" v-html="$options.svgSprite" />
</template>

<script>
const svgContext = require.context(
  '!svg-inline-loader?' +
    'removeTags=true' +
    '&removeSvgTagAttrs=true' +
    '&removingTagAttrs=fill' +
    '!@/assets/icons',
  true,
  /\w+\.svg$/i
)

const symbols = svgContext.keys().map((path) => {
  const id = path.replace(/^\.\/(.*)\.\w+$/, '$1')
  const content = svgContext(path)
  return content
    .replace('<svg', `<symbol id="${id}"`)
    .replace('svg>', 'symbol>')
})
export default {
  name: 'SvgSprite',
  svgSprite: symbols.join('\n')
}
</script>

<style scoped></style>
