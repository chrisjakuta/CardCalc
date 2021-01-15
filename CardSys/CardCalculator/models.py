from django.db import models
from django.utils.translation import gettext_lazy as _
import uuid
from decimal import Decimal
import CardSys.settings

class AirTimeProvider(models.Model):
    '''
    This model will house the type of provider.
    There are only three choices, MTN, GLO, AIRTEL.
    '''
    class Meta:
        verbose_name = 'Air Time Provider'
        verbose_name_plural = 'Air Time Providers'
    
    class Providers(models.TextChoices):
        AIRTIME_MTN = 'MTN', 'AirTimeMTN',
        AIRTIME_GLO = 'GLO', 'AirTimeGLO',
        AIRTIME_AIRTEL = 'AIRTEL', 'AirTimeAirtel',
    
    class CardTypes(models.TextChoices):
        _500 = '500', '_500_CARD',
        _200 = '200', '_200_CARD',
        _100 = '100', '_100_CARD',
    
    class CardPacks(models.TextChoices):
        TEN = '10', '_10_Pack',
        TWENTY = '20', '_20_Pack',
    
    type = models.CharField(
        _('Type'),
        max_length=50,
        choices=Providers.choices,
        default=None,
        help_text=_('The type of provider available, from one of the Providers.choices object.')
    )
    name = models.CharField(
        _('Name'),
        max_length=254,
        help_text=_('The name of the Provider in plain text.')
    )
    card_type = models.CharField(
        _('Card_Type'),
        max_length=254,
        choices=CardTypes.choices,
        default=None,
        help_text=_('The type of card -> 500, 200, or 100')
    )
    card_pack = models.CharField(
        _('Card Pack'),
        max_length=254,
        choices=CardPacks.choices,
        default=None,
        help_text=_('The type of pack these cards come in, either 10 or 20 cards in each pack')
    )
    card_pack_quantity = models.PositiveIntegerField(
        default=0,
        help_text=_('How many card packs are available?')
    ) #-> will hold how many card packs are available

    def __unicode__(self):
        return f'This is a {self.type} card of type {self.card_type} with {self.card_pack_quantity} available.' 
    
    def __repr__(self):
        return '<class \'CardSys.CardCalculator.models.AirTimeProvider\'>'
    
    @property
    def _type(self):
        return self.type
    
    @_type.setter
    def _type(self, value):
        self.type = value if value is bool else self.type
    
    @property
    def _card_type(self):
        return self.card_type
    
    @_card_type.setter
    def _card_type(self, value):
        self.card_type = value if value is bool else self.card_type
    
    @property
    def _card_pack(self):
        return self.card_pack
    
    @_card_pack.setter
    def _card_pack(self, value):
        self.card_pack = value if value is bool else self.card_pack
    
    @property
    def _card_pack_quantity(self):
        return self.card_pack_quantity
    
    @_card_pack_quantity.setter
    def _card_pack_quantity(self, value):
        self.card_pack_quantity = value if value is int else self.card_pack_quantity

class MTNProvider(AirTimeProvider):
    '''
    This is the object for MTN providers,
    will be a proxy model to AirTimeProvider,
    and inherit all methods and attributes.
    '''
    class Meta:
        verbose_name = 'MTN Card'
        verbose_name_plural =   'MTN Cards'
    CARD_PRICES = {
        '500': 550,
        '200': 220,
        '100': 110
    }

    def __unicode__(self):
        return self.name

    def _price_per_pack(self):
        if self.card_type in self.CARD_PRICES:
            price = self.CARD_PRICES[self.card_type]
            return price * int(self.card_pack)
        raise ValueError('Invalid Card Type.')

class GLOProvider(AirTimeProvider):
    '''
    This is the object for GLO providers,
    will be a proxy model to AirTimeProvider,
    and inherit all methods and attributes.
    '''
    class Meta:
        verbose_name = 'GLO Card'
        verbose_name_plural =   'GLO Cards'
    CARD_PACK_PRICES = {
        '500': 550,
        '200': 210,
        '100': 110
    }

    def __unicode__(self):
        return self.name
    
    def _price_per_pack(self):
        if self.card_type in self.CARD_PRICES:
            price = self.CARD_PRICES[self.card_type]
            return price * int(self.card_pack)
        raise ValueError('Invalid Card Type.')

class AIRTELProvider(AirTimeProvider):
    '''
    This is the object for AIRTEL providers,
    will be a proxy model to AirTimeProvider,
    and inherit all methods and attributes.
    '''
    class Meta:
        verbose_name = 'AIRTEL Card'
        verbose_name_plural =   'AIRTEL Cards'
    CARD_PACK_PRICES = {
        '500': 550,
        '200': 220,
        '100': 110
    }
    
    def __unicode__(self):
        return self.name

    def _price_per_pack(self):
        if self.card_type in self.CARD_PRICES:
            price = self.CARD_PRICES[self.card_type]
            return price * int(self.card_pack)
        raise ValueError('Invalid Card Type.')

class AirtimeCardPurchase(models.Model):
    '''
    This is the class meant to represent 
    any kind of airtime card, 
    that is sold in this store.
    This model will represent a card
    being sold at purcahes time, and
    will have a universally unique id.
    '''

    class Meta:

        verbose_name = 'Air Time Card Purchase'
        verbose_name_plural =  'Air Time Card Purchases'
    # here is where we put the type logic
    # provider will be a foreignkey to a provider
    provider = models.ForeignKey(
        AirTimeProvider,
        on_delete=models.CASCADE,
        related_name='purchased',
    )
    # a universally unique id -> used to identify
    # a group of air cards
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    total_balance = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        help_text=_('The total balance for all card packs purchased. ')
    )
    # we need to set up AUTH_USER_MODEL in settings and pass it here
    # purchased_by = models.ForeignKey()

    def __unicode__(self):
        pass
