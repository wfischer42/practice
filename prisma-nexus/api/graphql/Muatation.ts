import { schema } from "nexus";
import { prisma } from "nexus-plugin-prisma";

schema.mutationType({
  definition(t){
    t.crud.createOnePost()
    t.crud.createOneUser()

    t.field('createDraft', {
      type: 'Post',
      args: {
        title: schema.stringArg({nullable: false}),
        content: schema.stringArg(),
        authorEmail: schema.stringArg({nullable: false})
      },
      resolve: (parent, {authorEmail, content, title}, ctx) => {
        return ctx.db.post.create({data: { author: { create: { email: authorEmail } }, title, content } } )
      }
    })
  }
})