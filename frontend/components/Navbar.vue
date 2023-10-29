<template>
  <UiCard>
    <UiCardContent class="flex justify-between p-3">
      <ul class="flex gap-x-3">
        <NavbarItem to="/" name="Início" />
        <NavbarItem to="/discipline" name="Disciplinas" />
        <NavbarItem to="/user" name="Usuários" />
      </ul>

      <ul class="flex gap-x-3">
        <NavbarItem to="/profile" name="Perfil" />
      </ul>
    </UiCardContent>
  </UiCard>
</template>
