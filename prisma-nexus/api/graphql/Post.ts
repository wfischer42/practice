import {schema} from 'nexus'

schema.objectType({
  name: "Post",
  definition(t){
    t.model.id()
    t.model.content()
    t.model.published()
    t.model.title()
    t.model.author()
    t.model.createdAt()
  }
})

schema.objectType({
  name: 'User',
  definition(t){
    t.model.email()
    t.model.id()
    t.model.name()
    t.model.posts()
    t.model.profile()
  }
})

schema.objectType({
  name: "Profile",
  definition(t){
    t.model.user()
    t.model.id()
    t.model.bio()
  }
})

