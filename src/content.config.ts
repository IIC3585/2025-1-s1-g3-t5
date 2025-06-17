import { defineCollection, z } from 'astro:content';

const autores = defineCollection({
  type: 'content',
  schema: z.object({
    id: z.number(),
    name: z.string(),
    birthDate: z.string(),
    placeOfBirth: z.string(),
    gender: z.string(),
    country: z.string(),
    languages: z.array(z.string()),
    occupation: z.array(z.string()),
    genre: z.array(z.string()),
    image: z.string(),
    description: z.string()
  }),

});

const aves = defineCollection({
  type: 'data',
  schema: z.object({
    uid: z.string(),
    spanishName: z.string(),
    latinName: z.string(),
    englishName: z.string(),
    image: z.string(),
    description: z.string(),
    habitat: z.string(),
    didyouknow: z.string(),
    iucn: z.string(),
    size: z.string(),
    geo: z.string()
  }),

});

export const collections = {
  autores,
  aves
};
