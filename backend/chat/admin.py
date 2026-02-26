from django.contrib import admin
from .models import ChatRoom, Message, UserPresence, MessageReaction


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'updated_at')
    list_filter = ('created_at',)
    search_fields = ('id',)
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'sender', 'is_read', 'is_edited', 'is_deleted', 'created_at')
    list_filter = ('is_read', 'is_edited', 'is_deleted', 'created_at')
    search_fields = ('content', 'sender__username')
    readonly_fields = ('id', 'created_at', 'updated_at')


@admin.register(UserPresence)
class UserPresenceAdmin(admin.ModelAdmin):
    list_display = ('user', 'is_online', 'last_seen', 'current_room')
    list_filter = ('is_online',)
    search_fields = ('user__username',)


@admin.register(MessageReaction)
class MessageReactionAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'emoji', 'created_at')
    list_filter = ('emoji', 'created_at')
    search_fields = ('user__username',)
    readonly_fields = ('created_at',)
