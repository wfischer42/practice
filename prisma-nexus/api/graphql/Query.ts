import { schema } from 'nexus'

schema.queryType({
  definition(t) {
    t.field('drafts', {
      nullable: false,
      type: 'Post',
      list: true,
      resolve: (parent, args, ctx) => ctx.db.post.findMany()
    })
    t.field('users', {
      type: 'User',
      list: true,
      resolve: (parent, args, ctx) => ctx.db.user.findMany()
    })
  }
})
