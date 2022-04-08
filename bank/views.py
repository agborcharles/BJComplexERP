from django.shortcuts import render
from .models import *

from django.contrib.messages.views import SuccessMessageMixin

from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView, View
from django.urls import reverse_lazy

# Create your views here.


def bank_view(request):

    bank_accounts = BankAccount.objects.all()


    template_name = 'bank/accounts.html'
    context = { 'bank_accounts':bank_accounts,
                }
    return render(request, template_name, context)


def bank_transactions(request):

    deposit = Deposit.objects.all()
    withdrawal = Withdrawal.objects.all()
    bank_charges = BankCharges.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date:
        total_deposits = list(deposit.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        deposits = deposit.filter(created__range=[start_date, end_date])

        total_withdrawals = list(withdrawal.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        withdrawals = withdrawal.filter(created__range=[start_date, end_date])

        total_bank_charges = list(bank_charges.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]
        bank_charges= bank_charges.filter(created__range=[start_date, end_date])


    else:
        deposits = deposit
        total_deposits = list(deposit.aggregate(Sum('amount')).values())[0]

        withdrawals = withdrawal
        total_withdrawals = list(withdrawal.aggregate(Sum('amount')).values())[0]

        bank_charges = bank_charges
        total_bank_charges = list(bank_charges.aggregate(Sum('amount')).values())[0]


    template_name = 'bank/index.html'
    context = { 'deposits':deposits,
                'withdrawals':withdrawals,
                'bank_charges':bank_charges,

                'total_deposits':total_deposits,
                'total_withdrawals':total_withdrawals,
                'total_bank_charges':total_bank_charges,
                }
    return render(request, template_name, context)


def bank_account_details(request, slug):
    bank_account = BankAccount.objects.get(slug=slug)

    bank_opening_bal = bank_account.bankopeningbal_set.all()
    deposits = bank_account.deposit_set.all()
    withdrawals = bank_account.withdrawal_set.all()
    charges = bank_account.bankcharges_set.all()

    # DateTime Filter
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')



    if start_date:
        bank_opening_bal = list(bank_opening_bal.aggregate(Sum('amount')).values())[0]

        deposits = deposits.filter(created__range=[start_date, end_date])
        total_deposits = list(deposits.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        withdrawals = withdrawals.filter(created__range=[start_date, end_date])
        total_withdrawals = list(withdrawals.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        charges = charges.filter(created__range=[start_date, end_date])
        total_charges = list(charges.filter(created__range=[start_date, end_date]).aggregate(Sum('amount')).values())[0]

        account_bal = total_deposits - total_withdrawals
    else:
        bank_opening_bal = list(bank_opening_bal.aggregate(Sum('amount')).values())[0]

        deposits = deposits
        total_deposits = list(deposits.aggregate(Sum('amount')).values())[0]

        withdrawals = withdrawals
        total_withdrawals = list(withdrawals.aggregate(Sum('amount')).values())[0]

        charges = charges
        total_charges = list(charges.aggregate(Sum('amount')).values())[0]

        account_bal = bank_opening_bal + total_deposits - total_withdrawals - total_charges

    template_name = 'bank/accounts-profile.html'
    context = {
                'bank_account':bank_account,
                'bank_opening_bal':bank_opening_bal,

                'deposits':deposits,
                'total_deposits':total_deposits,

                'withdrawals':withdrawals,
                'total_withdrawals':total_withdrawals,

                'charges':charges,
                'total_charges':total_charges,

                'account_bal':account_bal,
                }

    return render(request, template_name, context)

class add_deposit(SuccessMessageMixin, CreateView):
    model = Deposit
    template_name = 'bank/forms/add_deposit.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Deposit Tranasction Successful !!!'

class edit_deposit(SuccessMessageMixin, UpdateView):
    model = Deposit
    template_name = 'bank/forms/edit_deposit.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Deposit Tranasction Successful Update !!!'

class add_withdrawal(SuccessMessageMixin, CreateView):
    model = Withdrawal
    template_name = 'bank/forms/add_withdrawal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Deposit Tranasction Successful !!!'

class edit_withdrawal(SuccessMessageMixin, UpdateView):
    model = Deposit
    template_name = 'bank/forms/edit_withdrawal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Deposit Tranasction Successful Update !!!'

class add_account_opening_bal(SuccessMessageMixin, CreateView):
    model = BankOpeningBal
    template_name = 'bank/forms/add_bank_opening_bal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'A/c Opening Bal Tranasction Successful !!!'

class edit_account_opening_bal(SuccessMessageMixin, UpdateView):
    model = BankOpeningBal
    template_name = 'bank/forms/edit_bank_opening_bal.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'A/c Opening Bal Tranasction Successfully Update !!!'

class add_bank_charges(SuccessMessageMixin, CreateView):
    model = BankOpeningBal
    template_name = 'bank/forms/add_bank_charges.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Bank Charges Tranasction Successfully Update !!!'


class edit_bank_charges(SuccessMessageMixin, UpdateView):
    model = BankOpeningBal
    template_name = 'bank/forms/edit_bank_charges.html'
    fields = '__all__'
    exclude = ('slug',)
    success_url = reverse_lazy('bank:bank-transactions')
    success_message = 'Bank Charges Tranasction Successfully Update !!!'
